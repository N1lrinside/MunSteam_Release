from django.urls import path
from .views import MainPage, Game

app_name = 'games'

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('game/<int:int>', Game.as_view(), name='game')
]