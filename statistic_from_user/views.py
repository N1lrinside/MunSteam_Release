from django.views import View
from django.shortcuts import render

from friends.service import get_friends, get_info_friends
from .service import ur_statistic, get_stats_in_game
from .models import GameStats
from friends.models import UserFriends
from user.utils import SteamURLRequiredMixin


class YourStatisticView(SteamURLRequiredMixin, View):
    template_name = 'statistic_from_user.html'

    def get(self, request):
        user = request.user
        statistic = ur_statistic(user.steam_id)
        return render(request, self.template_name, context={
            'statistic': statistic,
        })

    def post(self, request):
        pass


class ChoiseView(SteamURLRequiredMixin, View):
    template_name = 'choice.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass


class StatisticWithFriendsView(SteamURLRequiredMixin, View):
    template_name = 'statistic_with_friend.html'

    def get(self, request):
        user = request.user
        statistic = ur_statistic(user.steam_id)
        friends, text = get_info_friends(user.steam_id)
        statistic_friend = []
        if request.GET.get('friend'):
            get_stats_in_game(request.GET.get('friend'))
            statistic_friend = ur_statistic(request.GET.get('friend'))
        return render(request, self.template_name, context={
            'stat': statistic,
            'friends': friends,
            'stat_friend': statistic_friend,
            'text': text,
        })

    def post(self, request):
        pass
