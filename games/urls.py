from django.urls import path

from .views import MainView, GameView

app_name = 'games'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('game/<app_id:int>', GameView.as_view(), name='game')
]