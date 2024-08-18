from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.edit import CreateView
from user.forms import RegisterForm, LoginUserForm
from django.urls import reverse_lazy


# Create your views here.
@login_required
def profile(request):
    return render(request, 'pers_account.html')


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



'''def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': form})
'''
