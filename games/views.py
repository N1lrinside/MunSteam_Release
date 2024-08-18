from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import *


class MainPage(ListView):
    model = GameSteam
    template_name = 'mainpage.html'
    queryset = GameSteam.objects.order_by('name')


class Game(View):
    def get(self, request, int):
        game = GameSteam.objects.get(app_id=int)
        return render(request, 'gamepage.html', {
            'game': game
        })


def rel_shit(request, slug):
    return render(request, 'mainpage.html')