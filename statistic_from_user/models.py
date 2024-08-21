from django.db import models

from user.models import SteamUser


class GameStats(models.Model):
    user = models.ForeignKey(SteamUser, on_delete=models.CASCADE)
    game_id = models.IntegerField(default=730)
    total_kills = models.IntegerField(null=True)
    total_deaths = models.IntegerField(null=True)
    total_time_played = models.IntegerField(null=True)
    total_planted_bombs = models.IntegerField(null=True)
    total_defused_bombs = models.IntegerField(null=True)
    total_wins = models.IntegerField(null=True)
    total_damage_done = models.IntegerField(null=True)
    total_money_earned = models.IntegerField(null=True)
    total_wins_pistolround = models.IntegerField(null=True)
    total_mvps = models.IntegerField(null=True)
    total_matches_won = models.IntegerField(null=True)
    total_matches_played = models.IntegerField(null=True)

    def __str__(self):
        return self.user.personaname

    def money_earned(self):
        return str(self.total_money_earned) + '$'

    def time_played_hours(self):
        return (str(self.total_time_played // 3600) + ' часов '
                + str(self.total_time_played // 60 % 60) + ' минут')
