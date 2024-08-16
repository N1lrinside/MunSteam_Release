from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from user.forms import RegisterForm, LoginUserForm
from django.urls import reverse_lazy


# Create your views here.
@login_required
def profile(request):
    return render(request, 'pers_account.html')


class RegisterView(FormView):
    form_class = RegisterForm()
    template_name = 'registration/register.html'
    success_url = reverse_lazy("account")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
