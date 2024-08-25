from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .service import get_friend_info, get_friends_list
from .models import UserFriends


class FriendsView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        data = get_friends_list(user.steam_id)
        info_friends = []
        for i in data:
            info_friend = get_friend_info(i['steamid'])
            info_friend.update({'friend_since': i['friend_since']})
            info_friends.append(info_friend)
        UserFriends.objects.update_or_create(
            steam_id_user=user.steam_id,
            defaults={
                'friends_info': info_friends,
            }
        )

        return render(request, 'friendspage.html', context={
            'friends_info': info_friends,
        })

    def post(self, request):
        pass
