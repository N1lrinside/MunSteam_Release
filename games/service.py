import requests
from datetime import datetime, timezone
from googletrans import Translator

from django.conf import settings

from .models import GameSteam

translator = Translator()
steam_api_key = settings.API_KEY


def get_data_from_api(url, app_id=730, steam_id=0, count=3):
    params = {
        'key': steam_api_key,
        'appid': app_id,
        'count': count,
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
    data = response.json()
    return data


def player_count():
    """
    Обновляет кол-во игроков в игре в базе данных
    """
    apps_id = GameSteam.objects.values_list("app_id", flat=True)
    url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    for app_id in apps_id:
        print(app_id)
        data = get_data_from_api(url, app_id)
        try:
            players = data['response']['player_count']
        except KeyError:
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


'''
from bs4 import BeautifulSoup
from games.models import GameSteam
def check_page(app_id):
    url = f'https://store.steampowered.com/app/{app_id}//?l=russian'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # Извлечение названия игры
    title = soup.find('div', class_='apphub_AppName').text.strip()
    # Извлечение описания игры
    description = soup.find('div', class_='game_description_snippet').text.strip()
    # Извлечение URL изображения обложки
    cover_image_url = soup.find('img', class_='game_header_image_full')['src']
    # Извлечение жанров игры
    genres = [genre.text.strip() for genre in soup.find_all('a', class_='app_tag')]
    # Извлечение даты выхода
    release_date = soup.find('div', class_='date').text.strip()
    # Извлечение цены игры (если есть)
    price_section = soup.find('div', class_='game_purchase_price')
    if price_section:
        price = price_section.text.strip()
    else:
        price = 'Free'  # Если игра бесплатная
    # Печать результатов
    print(f"Название: {title}")
    print(f"Описание: {description}")
    print(f"Обложка: {cover_image_url}")
    print(f"Жанры: {genres}")
    print(f"Дата выхода: {release_date}")
    print(f"Цена: {price}")
    game, created = GameSteam.objects.update_or_create(
        app_id=app_id,
        defaults={
            'name': title,
            'description': description,
            'url_image': cover_image_url,
            'genre': ', '.join(genres),
            'release_date': release_date,
            'price': price,
        }
    )
    if created:
        print(f"Игра '{title}' была добавлена в базу данных.")
    else:
        print(f"Игра '{title}' была обновлена в базе данных.")
def games():
    check_page(431960)
    check_page(2139460)
    check_page(289070)
    check_page(1938090)'''



