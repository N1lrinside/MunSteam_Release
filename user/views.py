from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from user.forms import RegisterForm, LoginUserForm, SteamUrlForm
from .service import get_id, get_data_user


# Create your views here.
'''@login_required
def profile(request):
    return render(request, 'pers_account.html')'''


class ProfileView(LoginRequiredMixin, View):
    template_name = 'pers_account.html'

    def get(self, request):
        context = {
            'form': SteamUrlForm()
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = SteamUrlForm(request.POST)
        if form.is_valid():
            user = request.user
            steam_id = get_id(form.cleaned_data.get('profileurl'))
            user.steam_id = steam_id
            user.profileurl = form.cleaned_data.get('profileurl')
            user.personaname, user.avatarfull, user.personastate, user.profilestate, user.communityvisibilitystate, user.gameextrainfo, user.createdacc_time, user.lastlogoff_time = get_data_user(steam_id)
            user.save()
            return redirect('user:profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)


class RegisterView(View):
    template_name = 'registration/register.html'

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



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация'}



def detach_steam(request):
    if request.method == 'POST':
        user = request.user
        user.profileurl = None
        user.steam_id = None
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})