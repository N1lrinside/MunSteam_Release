
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
def main(request):
    name_game = request.GET.get('name_game')
    list_games = ['CS2', 'Dota2', 'PUBG']
    return render(request, 'statistic_from_user.html', {
        'name_game': name_game,
        'list_games': list_games
    })


class StatisticView(LoginRequiredMixin):
    template_name = 'statistic_from_user.html'

    def get(self, request):

        return render(request, self.template_name)