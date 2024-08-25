from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .service import get_stats_in_game, check_game_on_account, get_friends_user
from .models import GameStats
from friends.models import UserFriends


class StatisticView(LoginRequiredMixin, View):
    template_name = 'statistic_from_user.html'

    def get(self, request):
        user = request.user
        if user.check_auth() and check_game_on_account(user.steam_id):
            get_stats_in_game(user.steam_id)
            context = True
            stat = GameStats.objects.filter(user_steam_id=user.steam_id).get()
            friends = get_friends_user(user.steam_id)
            if request.GET.get('friend'):
                check = True
                get_stats_in_game(request.GET.get('friend'))
                stat_friend = GameStats.objects.filter(user_steam_id=request.GET.get('friend')).get()
            else:
                check = False
                stat_friend = "Не выбран друг"
        else:
            check = False
            context = False
            stat = "Ваш стим аккаунт не привязан или У вас нет CS2"
            stat_friend = "Не выбран друг"
        return render(request, self.template_name, context={
            'context': context,
            'stat': stat,
            'friends': friends,
            'check': check,
            'stat_friend': stat_friend
        })

    def post(self, request):
        pass
