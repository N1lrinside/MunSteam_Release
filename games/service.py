import os
import requests
from datetime import datetime, timezone
from django.conf import settings
from .models import GameSteam


def player_count():
    apps_id = GameSteam.objects.values_list('app_id', flat=True)
    steam_api_key = settings.API_KEY
    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    for app_id in apps_id:
        params = {
            'key': steam_api_key,
            'appid': app_id
        }
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200 and 'response' in data:
            players = data['response']['player_count']
        else:
            players = 'Нет информации'

        GameSteam.objects.filter(app_id=app_id).update(players_in_game=players,
                                last_update=datetime.now(timezone.utc))
    print('Кол-во игроков обновлено')


def get_time():
    apps_id = GameSteam.objects.values_list('app_id', flat=True)
    for app_id in apps_id:
        time = GameSteam.objects.get(app_id=app_id)
        times = datetime.strptime(time.last_update[:19], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
        GameSteam.objects.filter(app_id=app_id).update(minutes_update=str(datetime.now(timezone.utc) - times))
    print('Время обновлено')