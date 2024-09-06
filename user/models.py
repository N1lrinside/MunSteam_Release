from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum


class SteamUser(AbstractUser):
    PERSONA_STATE_CHOICES = [
        (0, 'Оффлайн'),
        (1, 'Онлайн'),
        (2, 'Занят'),
        (3, 'Отсутствует'),
        (4, 'Отложен'),
        (5, 'Хочет обменять'),
        (6, 'Хочет поиграть'),
    ]

    PROFILE_STATE_CHOICES = [
        (1, 'Приватный'),
        (3, 'Общедоступный'),
    ]

    steam_id = models.CharField(max_length=20, null=True)
    personaname = models.CharField(max_length=255, null=True, blank=True, default='Нет информации')
    profileurl = models.URLField(null=True)
    avatarfull = models.URLField(null=True, blank=True, default='https://bootdey.com/img/Content/avatar/avatar7.png')
    personastate = models.IntegerField(choices=PERSONA_STATE_CHOICES, null=True, blank=True)
    profilestate = models.BooleanField(null=True, default=False)
    communityvisibilitystate = models.IntegerField(choices=PROFILE_STATE_CHOICES, null=True, blank=True)
    gameextrainfo = models.CharField(max_length=255, null=True, blank=True)
    createdacc_time = models.DateTimeField(null=True, blank=True)
    lastlogoff_time = models.DateTimeField(null=True, blank=True)
    last_update = models.DateField(null=True)
    last_update_url = models.DateTimeField(null=True)

    def check_auth(self):
        if self.profileurl is None:
            return False
        return True

    def check_status(self):
        if self.communityvisibilitystate == 1:
            return False
        return True


class UserRecentlyPlayedGames(models.Model):
    user_steam_id = models.CharField(max_length=50, null=True)
    app_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=50, null=True)
    playtime_2weeks = models.IntegerField(null=True)
    total_playtime_2weeks = models.IntegerField(null=True)
    percentage = models.FloatField(null=True)
    img_icon_url = models.URLField()

    def __str__(self):
        return self.user_steam_id + self.name

    def playtime_2weeks_hours(self):
        return round(self.playtime_2weeks / 60, 1)

    def total_playtime_2weeks_hours(self):
        return round(self.total_playtime_2weeks / 60, 1)

    class Meta:
        unique_together = ('user_steam_id', 'app_id')
