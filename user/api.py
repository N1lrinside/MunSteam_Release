from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import UserRecentlyPlayedGames, TelegramUser, SteamUser
from .serializers import RecentlyGamesSerializer, UserTelegramSerializer, UserInfoSerializer


class RecentlyGameView(ReadOnlyModelViewSet):
    queryset = UserRecentlyPlayedGames.objects.all()
    serializer_class = RecentlyGamesSerializer


class UserTelegramView(ReadOnlyModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = UserTelegramSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id',]


class UserInfoView(ReadOnlyModelViewSet):
    queryset = SteamUser.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['steam_id',]
