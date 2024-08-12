from django.urls import path
from .views import rel_shit, MainPage, Game

urlpatterns = [
    path('', MainPage.as_view(), name='games'),
    path('game/<int:int>', Game.as_view(), name='game')
]