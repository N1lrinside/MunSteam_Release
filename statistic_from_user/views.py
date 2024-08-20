from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .service import get_stats_in_game


class StatisticView(LoginRequiredMixin, View):
    template_name = 'statistic_from_user.html'

    def get(self, request):
        user = request.user
        if user.check_auth():
            get_stats_in_game(user.steam_id, user)
            context = "Успешно"
        else:
            context = 'Ваш профиль стим не привязан'
        return render(request, self.template_name, context={
            'context': context
        })

    def post(self, request):
        pass