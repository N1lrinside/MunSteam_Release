from django.shortcuts import render
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from .service import get_info_friends
from .serializer import FriendsSerializer
from .models import UserFriends
from user.utils import SteamURLRequiredMixin


class FriendsView(SteamURLRequiredMixin, View):

    def get(self, request):
        user = request.user
        info_friends, text = get_info_friends(user.steam_id)
        return render(request, 'friendspage.html', context={
            'friends_info': info_friends,
            'text': text
        })

    def post(self, request):
        pass


#------------------API----------------------
class FriendsListView(ReadOnlyModelViewSet):
    queryset = UserFriends.objects.all()
    serializer_class = FriendsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['steam_id_user', ]
