from datetime import datetime

import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('STEAM_API')
id_user = '76561198821788610'

url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'

params = {
    'key': api_key,
    'steamids': id_user
}

response = requests.get(url, params=params)
for data in response.json()['response']['players']:
    lastlogoff_unix = data.get('lastlogoff')
    if lastlogoff_unix:
        lastlogoff_time = datetime.fromtimestamp(lastlogoff_unix)
        createdacc_time = datetime.fromtimestamp(data.get('timecreated'))
        print("Создание акка:", createdacc_time.strftime('%Y-%m-%d %H:%M:%S'))
        print("Последний выход:", lastlogoff_time.strftime('%Y-%m-%d %H:%M:%S'))
    print("Steam ID:", data.get('steamid'))
    print("Имя профиля (Никнейм):", data.get('personaname'))
    print("URL профиля:", data.get('profileurl'))
    print("Аватар (большой):", data.get('avatarfull'))
    print("Статус (Онлайн/Офлайн):", data.get('personastate'))
    print("ID основной группы:", data.get('primaryclanid'))
    print("Состояние профиля:", data.get('profilestate'))
    print("Уровень видимости профиля:", data.get('communityvisibilitystate'))
    print("имя игры", data.get('gameextrainfo'))
