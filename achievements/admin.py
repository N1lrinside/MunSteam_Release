from django.contrib import admin

from .models import GameUser, GameAchievement

admin.site.register(GameUser)
admin.site.register(GameAchievement)
