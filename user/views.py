from datetime import date, datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import RegisterForm, LoginUserForm, SteamUrlForm, UserPasswordChangeForm
from .service import get_id, get_data_user, get_recently_games, detach_steam, connect_telegram, check_update_url, reset_update_url
from .tasks import update_info


class ProfileView(LoginRequiredMixin, View):
    template_name = 'pers_account.html'

    def get(self, request):
        user = request.user
        connect_telegram(request)
        reset_update_url(request, user)
        context = check_update_url(user)
        context['form'] = SteamUrlForm()
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = SteamUrlForm(request.POST)
        user = request.user
        if form.is_valid():
            steam_id = get_id(form.cleaned_data.get('profileurl'))
            user.steam_id = steam_id
            user.profileurl = form.cleaned_data.get('profileurl')
            info_user = get_data_user(steam_id)
            user.personaname, user.avatarfull, user.personastate, user.profilestate = info_user[:4]
            user.communityvisibilitystate, user.gameextrainfo, user.createdacc_time, user.lastlogoff_time = info_user[4:]
            update_info.delay(steam_id)
            user.last_update_url = datetime.now()
            user.last_update = None
            get_recently_games(steam_id)
            user.save()
            return redirect('user:profile')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)


class RegisterView(View):
    template_name = 'registration_temp/register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user:profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'registration_temp/login.html'
    extra_context = {'title': 'Авторизация'}


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = "registration_temp/password_change_form.html"
    success_url = reverse_lazy("user:password_change_done")


class DetachSteamView(LoginRequiredMixin, View):

    def get(self, request):
        pass

    def post(self, request):
        user = request.user
        detach_steam(user)
        return redirect('user:profile')


class UpdateView(LoginRequiredMixin, View):

    def get(self, request):
        pass

    def post(self, request):
        user = request.user
        update_info.delay(user.steam_id)
        user.last_update = date.today()
        user.save()
        return redirect('user:profile')
