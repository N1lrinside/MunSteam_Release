from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import GameUser
from .service import get_achievements, games_user
from user.utils import SteamURLRequiredMixin


class GameAchievementView(SteamURLRequiredMixin, ListView):
    model = GameUser
    template_name = 'gameachievements.html'
    context_object_name = 'games'

    def get_queryset(self):
        user = self.request.user
        queryset = GameUser.objects.filter(user_steam_id=user.steam_id).order_by('games')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['games'].exists():
            game_user = context['games'].first()
            context['game_list'] = [
                {'name': game_name, 'url': game_user.get_url(game_id)}
                for game_id, game_name in game_user.games.items()
            ]
        return context

    def post(self, request):
        pass


class AchievementsView(SteamURLRequiredMixin, View):

    def get(self, request, app_id):
        user = request.user
        game_name = games_user(user.steam_id)[app_id]
        achievements, count_achievements, count_achieved, percentage = get_achievements(user.steam_id, app_id, game_name)
        return render(request, 'achievement.html', context={
            'achievements': achievements,
            'count_achievements': count_achievements,
            'count_achieved': count_achieved,
            'percentage':  percentage,
            'game_name': game_name,
        })

    def post(self, request):
        pass
