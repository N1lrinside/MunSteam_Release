from django.db import models
from django.contrib.auth.models import AbstractUser


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

    steam_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    personaname = models.CharField(max_length=255, null=True, blank=True)
    profileurl = models.URLField(null=True, blank=True)
    avatarfull = models.URLField(null=True, blank=True)
    personastate = models.IntegerField(choices=PERSONA_STATE_CHOICES, null=True, blank=True)
    profilestate = models.IntegerField(choices=PROFILE_STATE_CHOICES, null=True, blank=True)
    communityvisibilitystate = models.IntegerField(choices=PROFILE_STATE_CHOICES, null=True, blank=True)
    gameextrainfo = models.CharField(max_length=255, null=True, blank=True)
    createdacc_time = models.DateTimeField(null=True, blank=True)
    lastlogoff_time = models.DateTimeField(null=True, blank=True)
