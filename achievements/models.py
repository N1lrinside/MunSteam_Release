from django.db import models
from django.urls import reverse_lazy

from user.models import SteamUser


class GameAchievement(models.Model):
    user = models.ForeignKey(SteamUser, on_delete=models.CASCADE)
    app_id = models.CharField(max_length=50, null=True)
    achievements = models.JSONField()

    def __str__(self):
        return self.user.username


class GameUser(models.Model):
    user_steam_id = models.CharField(max_length=50, unique=True, null=True)
    games = models.JSONField()

    def __str__(self):
        return self.user_steam_id

    def get_url(self, app_id):
        return reverse_lazy('achievements', kwargs={'app_id': app_id})