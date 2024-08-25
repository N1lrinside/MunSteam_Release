from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done',
         PasswordChangeDoneView.as_view(template_name='registration_temp/password_change_done.html'),
         name='password_change_done'),
    path('password-reset/',
         PasswordResetView.as_view(
            template_name='registration_temp/password_reset_form.html',
            email_template_name='registration_temp/password_reset_email.html',
            success_url=reverse_lazy("user:password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done',
         PasswordResetDoneView.as_view(template_name='registration_temp/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registration_temp/password_reset_confrim.html',
             success_url=reverse_lazy('user:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset/complete',
         PasswordResetCompleteView.as_view(template_name='registration_temp/password_reset_complete.html'),
         name='password_reset_complete'),
    path('detach-steam/', views.DetachSteamView.as_view(), name='detach_steam'),
    path('update-time/', views.UpdateView.as_view(), name='update_data')
]
