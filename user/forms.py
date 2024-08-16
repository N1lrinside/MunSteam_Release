from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().filter(email=email).exists():
            raise forms.ValidationError("На эту почту уже привязан аккаунт")
        return email

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']