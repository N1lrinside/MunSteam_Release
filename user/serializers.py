from rest_framework import serializers

from .models import UserRecentlyPlayedGames, SteamUser, TelegramUser


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


class UserTelegramSerializer(serializers.ModelSerializer):
    steamid_user = serializers.SerializerMethodField()

    def get_steamid_user(self, obj):
        user = SteamUser.objects.filter(steam_id=obj.user.steam_id).first()
        return user.steam_id

    class Meta:
        model = TelegramUser
        fields = ('telegram_id', 'steamid_user')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamUser
        fields = (
            'steam_id', 'personaname', 'profileurl', 'avatarfull', 'get_personastate_display',
            'get_communityvisibilitystate_display', 'createdacc_time', 'lastlogoff_time',
        )
