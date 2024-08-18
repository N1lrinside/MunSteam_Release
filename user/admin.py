from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from user.models import SteamUser


@admin.register(SteamUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'steam_id', 'personaname', 'profileurl', 'avatarfull', 'personastate', 'createdacc_time', 'lastlogoff_time')
    # Дополнительные настройки

