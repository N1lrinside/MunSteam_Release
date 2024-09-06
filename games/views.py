from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import GameSteam


class MainView(ListView):
    model = GameSteam
    template_name = 'main.html'
    queryset = GameSteam.objects.order_by('name')


class GameView(View):

    def get(self, request, app_id):
        game = GameSteam.objects.get(app_id=app_id)
        return render(request, 'game.html', {
            'game': game
        })

    def post(self, request):
        pass
