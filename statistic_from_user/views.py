from django.views import View
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from friends.service import get_friends, get_info_friends
from .service import ur_statistic, get_stats_in_game
from .models import GameStats
from .serializer import StatsSerializer
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


class StatisticView(ReadOnlyModelViewSet):
    queryset = GameStats.objects.all()
    serializer_class = StatsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_steam_id', ]

    def get_queryset(self):
        return self.queryset.exclude(
            total_kills__isnull=True,
            total_deaths__isnull=True,
            total_time_played__isnull=True,
            total_planted_bombs__isnull=True,
            total_defused_bombs__isnull=True,
            total_damage_done__isnull=True,
            total_money_earned__isnull=True,
            total_wins_pistolround__isnull=True,
            total_mvps__isnull=True,
            total_matches_won__isnull=True,
            total_matches_played__isnull=True
        )
