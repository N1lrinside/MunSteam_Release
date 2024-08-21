from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .service import get_stats_in_game, check_game_on_account
from .models import GameStats


class StatisticView(LoginRequiredMixin, View):
    template_name = 'statistic_from_user.html'

    def get(self, request):
        user = request.user
        if user.check_auth() and check_game_on_account(user.steam_id):
            get_stats_in_game(user.steam_id, user)
            context = True
            stat = GameStats.objects.filter(user=user).get()
        else:
            context = False
            stat = "Ваш стим аккаунт не привязан или У вас нет CS2"
        return render(request, self.template_name, context={
            'context': context,
            'stat': stat
        })

    def post(self, request):
        pass