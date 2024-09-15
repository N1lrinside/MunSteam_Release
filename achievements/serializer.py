from rest_framework import serializers

from .models import GameUser, GameAchievement


class GamesUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameUser
        fields = ('user_steam_id', 'games')


class AchievementsGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameAchievement
        fields = ('user_steam_id', 'app_id', 'game_name', 'achievements')
