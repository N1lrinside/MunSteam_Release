from django.db import models


class UserFriends(models.Model):
    steam_id_user = models.CharField(max_length=50, null=True, unique=True)
    friends_info = models.JSONField(null=True)

    def __str__(self):
        return self.steam_id_user
