import re
import requests


def get_id(steam_id):
    """
    Получение id профиля стим
    """
    url = f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/'
    params = {
        'key': 'A841CD672B51AB7D6C82A7CDA8B28E86',
        'count': 3,
        'maxlength': 1000,
        'format': 'json',
        'include_appinfo': True,
        'include_played_free_games': True,
        'steamid': steam_id,
        'steamids': steam_id,
        'vanityurl': steam_id,
        'relationship': 'friend',
    }
    response = requests.get(url, params=params)
    data = response.json().get('response', {}).get('games', [])
    return data


print(get_id(76561198371847461))
print(bool(None))
#  response.get('response', {}).get('steamid', id)