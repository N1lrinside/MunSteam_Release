from django.urls import path

from .views import MainView, GameView

app_name = 'games'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('game/<int:app_id>', GameView.as_view(), name='game')
]