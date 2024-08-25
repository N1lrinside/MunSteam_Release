from django.shortcuts import render
from django.views import View

from .service import get_friends
from user.utils import SteamURLRequiredMixin


class FriendsView(SteamURLRequiredMixin, View):

    def get(self, request):
        user = request.user
        info_friends, text = get_friends(user, user.steam_id)
        return render(request, 'friendspage.html', context={
            'friends_info': info_friends,
            'text': text
        })

    def post(self, request):
        pass
