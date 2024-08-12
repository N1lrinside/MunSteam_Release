from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user import models
from django import forms

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.UserSteam
        fields = UserCreationForm.Meta.fields + ('email', )

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']