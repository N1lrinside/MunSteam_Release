from datetime import datetime, timezone

from django.db import models
from django.urls import reverse


# Create your models here.
class GameSteam(models.Model):
    app_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url_image = models.URLField()
    genre = models.TextField()
    release_date = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    players_in_game = models.CharField(default='Нет информации')
    last_update = models.CharField(default=datetime.now(timezone.utc))
    minutes_update = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.app_id

    def get_url(self):
        return reverse('game', args=[self.app_id])

    def get_update_time(self):
        return str(int(self.minutes_update[2:4])) + ' минут назад'

    class Meta:
        verbose_name = 'GameSteam'

