import requests
import re
from datetime import datetime

from django.conf import settings

from games.service import get_data_from_api
from statistic_from_user.service import get_stats_in_game, check_game_on_account

api_key = settings.API_KEY


def get_id(url):
    """
    Получение id профиля стим
    """
    check_id = re.search(r'/id/', url)
    if check_id:
        id_profile = re.search(r'/id/\w+', url).group()[4:]
        url = f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
        response = get_data_from_api(url, steam_id=id_profile)
        id64 = response.get('response', {}).get('steamid', id)
    else:
        id64 = re.search(r'/profiles/\d+', url).group()[10:]
    return id64


def get_data_user(steam_id):
    """
    Получение информации о пользователе
    """
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    data = get_data_from_api(url, steam_id=steam_id)
    for info in data['response']['players']:
        last_logoff_unix = info.get('lastlogoff')
        if last_logoff_unix is not None:
            last_logoff_time = datetime.fromtimestamp(last_logoff_unix)
            created_acc_time = datetime.fromtimestamp(info.get('timecreated'))
        else:
            last_logoff_time = datetime.now()
            created_acc_time = datetime.now()
        return [
                info.get('personaname'),
                info.get('avatarfull'),
                info.get('personastate'),
                info.get('profilestate'),
                info.get('communityvisibilitystate'),
                info.get('gameextrainfo'),
                created_acc_time.strftime('%Y-%m-%d %H:%M:%S'),
                last_logoff_time.strftime('%Y-%m-%d %H:%M:%S'),
                ]


def update_info_user(steam_id):
    if check_game_on_account(steam_id):
        get_stats_in_game(steam_id)
