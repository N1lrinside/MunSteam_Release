import requests
from datetime import datetime, timezone
from googletrans import Translator

from django.conf import settings

from .models import GameSteam

translator = Translator()
steam_api_key = settings.API_KEY


def get_data_from_api(url, app_id=730, steam_id=0):
    params = {
        'key': steam_api_key,
        'appid': app_id,
        'count': 3,
        'maxlength': 1000,
        'format': 'json',
        'include_appinfo': True,
        'include_played_free_games': True,
        'steamid': steam_id,
        'steamids': steam_id,
        "vanityurl": steam_id,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


def player_count():
    """
    Обновляет кол-во игроков в игре в базе данных
    """
    apps_id = GameSteam.objects.values_list("app_id", flat=True)
    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    for app_id in apps_id:
        data = get_data_from_api(url, app_id)
        if "response" in data:
            players = data['response']['player_count']
        else:
            players = "Нет информации"

        GameSteam.objects.filter(app_id=app_id).update(
            players_in_game=players,
            last_update_players=datetime.now(timezone.utc)
            )
    print("Кол-во игроков обновлено")


def get_time():
    """
    Обновляет время запроса в базе данных
    """
    apps_id = GameSteam.objects.values_list('app_id', flat=True)
    for app_id in apps_id:
        time = GameSteam.objects.get(app_id=app_id)
        times = datetime.strptime(time.last_update_players[:19], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
        GameSteam.objects.filter(app_id=app_id).update(minutes_update=str(datetime.now(timezone.utc) - times))
    print("Время обновлено")


def get_news_game():
    url = 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
    apps_id = GameSteam.objects.values_list('app_id', flat=True)
    for app_id in apps_id:
        data = get_data_from_api(url, app_id)
        news = {translator.translate(i['title'], src='en', dest='ru').text: translator.translate(i['contents'], src='en', dest='ru').text.replace("{STEAM_CLAN_IMAGE}", "https://clan.akamai.steamstatic.com/images/") for i in data['appnews']['newsitems']}
        news_update = datetime.now()
        GameSteam.objects.filter(app_id=app_id).update(news=news, last_update_news=news_update)
        print(f'Новости обновлены для {app_id}')

