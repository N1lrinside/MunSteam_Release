from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserSteam(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='usersteam_set',  # Измените related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usersteam',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usersteam_permissions',  # Измените related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usersteam',
    )