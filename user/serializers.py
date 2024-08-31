from rest_framework import serializers

from .models import UserRecentlyPlayedGames, SteamUser


class RecentlyGamesSerializer(serializers.ModelSerializer):
    name_user = serializers.SerializerMethodField()
    steamid_user = serializers.SerializerMethodField()

    def get_name_user(self, obj):
        user = SteamUser.objects.filter(steam_id=obj.user_steam_id).first()
        return user.personaname

    def get_steamid_user(self, obj):
        return obj.user_steam_id

    class Meta:
        model = UserRecentlyPlayedGames
        fields = ('id', 'name', 'app_id', 'name_user', 'steamid_user', 'playtime_2weeks', 'total_playtime_2weeks', 'percentage')

