from django.conf import settings

from .models import GameStats
from games.service import get_data_from_api

api_key = settings.API_KEY


def get_stats_in_game(steam_id, app_id=730):
    """
    Запрос на получение и сохранение статистки пользователя в игре
    """
    fields = ['total_kills', 'total_deaths', 'total_time_played', 'total_planted_bombs', 'total_defused_bombs',
              'total_winxs', 'total_damage_done', 'total_money_earned', 'total_wins_pistolround', 'total_mvps',
              'total_matches_won', 'total_matches_played']
    url = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/"
    data = get_data_from_api(url, app_id, steam_id)
    stats = data.get("playerstats", {}).get('stats', [])
    stats_dict = {stat.get('name'): stat.get('value') for stat in stats if stat.get('name') in fields}
    if not GameStats.objects.filter(user_steam_id=steam_id).exists():
        GameStats.objects.create(
            user_steam_id=steam_id,
            game_id=app_id,
            **stats_dict
        )
    else:
        GameStats.objects.update_or_create(
            user_steam_id=steam_id,
            game_id=app_id,
            defaults=stats_dict
        )


def check_game_on_account(steam_id, app_id=730):
    """
    Проверка есть ли игра у пользователя
    """
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    data = get_data_from_api(url, app_id, steam_id)
    games = data.get('response', {}).get('games', [])
    for game in games:
        if game['appid'] == app_id:
            return True
    return False
