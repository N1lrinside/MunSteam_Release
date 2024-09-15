from rest_framework import serializers

from .models import GameStats

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStats
        fields = (
            'user_steam_id', 'total_kills', 'total_deaths', 'time_played_hours', 'total_planted_bombs',
            'total_defused_bombs', 'total_damage_done', 'money_earned', 'total_wins_pistolround',
            'total_mvps', 'total_matches_won', 'total_matches_played'
        )
