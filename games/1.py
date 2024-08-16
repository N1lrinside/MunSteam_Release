'''from bs4 import BeautifulSoup
from games.models import GameSteam
import requests

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
    check_page(570)
    check_page(730)
    check_page(252490)
    check_page(578080)
    check_page(105600)
    check_page(1966720)
    check_page(271590)
    check_page(252950)
games()'''