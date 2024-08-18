from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .service import get_id


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("На эту почту уже привязан аккаунт")
        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class SteamUrlForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profileurl', )
        widgets = {
            'profileurl': forms.TextInput(attrs={'style': 'width: 400px;'})
        }

    def clean_profileurl(self):
        url = self.cleaned_data['profileurl']
        if get_user_model().objects.filter(profileurl=url).exists():
            raise forms.ValidationError("Этот стим аккаунт уже привязан")

        steam_id = get_id(url)
        if get_user_model().objects.filter(steam_id=steam_id).exists():
            raise forms.ValidationError("Этот стим аккаунт уже привязан к другому пользователю")

        self.cleaned_data['steam_id'] = steam_id

        return url