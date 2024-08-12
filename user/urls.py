from django.contrib.auth.views import LogoutView
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout")
]
