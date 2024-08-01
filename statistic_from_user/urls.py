from django.urls import path
from statistic_from_user import views


urlpatterns = [
    path('', views.main, name='home')
]
