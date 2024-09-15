from django.contrib import admin

from user.models import SteamUser, UserRecentlyPlayedGames, TelegramUser


@admin.register(SteamUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'steam_id', 'personaname', 'profileurl', 'avatarfull', 'personastate', 'createdacc_time', 'lastlogoff_time')


admin.site.register(UserRecentlyPlayedGames)
admin.site.register(TelegramUser)
