from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import GameUser, GameAchievement
from .service import get_achiviements_game


class GameAchievementView(LoginRequiredMixin, ListView):
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


class AchievementsView(LoginRequiredMixin, View):

    def get(self, request, app_id):
        user = request.user
        achiv_exists = GameAchievement.objects.filter(user=user, app_id=app_id)
        if achiv_exists.exists():
            exists = True
            achievements = achiv_exists.first().achievements
            count_achievements = len(achievements)
            count_achieved = len([i for i in achievements if i['achieved']])
            percentage = (count_achieved / count_achievements) * 100
        else:
            exists = True
            achievements = get_achiviements_game(user.steam_id, app_id)
            if achievements:
                count_achievements = len(achievements)
                count_achieved = len([i for i in achievements if i['achieved']])
                percentage = (count_achieved / count_achievements) * 100
                achiv_exists.update_or_create(
                    user=user,
                    app_id=app_id,
                    achievements=achievements
                )
            else:
                exists = False
                count_achievements = 0
                count_achieved = 0
                percentage = 0

        return render(request, 'achievement.html', context={
            'achievements': achievements,
            'exists': exists,
            'count_achievements': count_achievements,
            'count_achieved': count_achieved,
            'percentage':  percentage
        })

    def post(self, request):
        pass
