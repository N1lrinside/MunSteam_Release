import pytz
import re
from datetime import datetime, timedelta, date

from django.conf import settings
from django.db.models import Sum

from .models import UserRecentlyPlayedGames, TelegramUser
from achievements.models import GameUser
from achievements.service import games_user
from friends.service import get_friends
from games.service import get_data_from_api
from statistic_from_user.service import get_stats_in_game, check_game_on_account

api_key = settings.API_KEY


def get_id(url):
    """
    Получение id профиля стим
    """
    check_id = re.search(r'https://steamcommunity.com/id/', url)
    if check_id:
        id_profile = re.search(r'/id/\w+', url).group()[4:]
        url = f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
        response = get_data_from_api(url, steam_id=id_profile)
        id64 = response.get('response', {}).get('steamid', id)
    else:
        id64 = re.search(r'https://steamcommunity.com/profiles/\d+', url).group()[36:]
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


def get_recently_games(steam_id):
    """
    Получение последней статистики пользователя за 2 недели
    """
    url = f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/'
    data_api = get_data_from_api(url, steam_id=steam_id, count=5)
    data = data_api.get('response', {}).get('games', [])
    for game in data:
        UserRecentlyPlayedGames.objects.update_or_create(
            user_steam_id=steam_id,
            app_id=game['appid'],
            defaults={
                'name': game['name'],
                'playtime_2weeks': game['playtime_2weeks'],
                'img_icon_url': 'https://media.steampowered.com/steamcommunity/public/images/apps/' + str(
                    game['appid']) + '/' + game['img_icon_url'] + '.jpg',
            }
        )
    total_playtime = \
    UserRecentlyPlayedGames.objects.filter(user_steam_id=steam_id).aggregate(total=Sum('playtime_2weeks'))['total']

    # Обновляем каждую запись, чтобы пересчитать процент
    games = UserRecentlyPlayedGames.objects.filter(user_steam_id=steam_id)
    for game in games:
        if total_playtime > 0:  # Проверяем, чтобы избежать деления на ноль
            percentage = (game.playtime_2weeks / total_playtime) * 100
        else:
            percentage = 0

        game.total_playtime_2weeks = total_playtime
        game.percentage = percentage
        game.save(update_fields=['total_playtime_2weeks', 'percentage'])


def detach_steam(user):
    user.steam_id = None
    user.personaname = 'Нет информации'
    user.profileurl = None
    user.avatarfull = 'https://bootdey.com/img/Content/avatar/avatar7.png'
    user.personastate = None
    user.profilestate = False
    user.communityvisibilitystate = None
    user.gameextrainfo = None
    user.createdacc_time = None
    user.lastlogoff_time = None
    user.save()


def connect_telegram(request):
    telegram_id = request.GET.get('telegram_id')
    if telegram_id:
        profile, created = TelegramUser.objects.update_or_create(
            user=request.user,
            defaults={'telegram_id': telegram_id}
        )
        if created:
            print("Создан новый профиль TelegramUser")
        else:
            print("Профиль TelegramUser обновлён")


def check_update_url(user):
    response = UserRecentlyPlayedGames.objects.filter(user_steam_id=user.steam_id)
    if response.exists():
        games = response.order_by('-playtime_2weeks')
        total_playtime = response.first()
    else:
        games = []
        total_playtime = 0
    if bool(user.last_update_url):
        time_diff = datetime.now(pytz.timezone('Europe/Moscow')) - user.last_update_url
        can_detach = time_diff >= timedelta(hours=3)
        context = {
            'today': date.today(),
            'can_detach': can_detach,
            'time_diff': time_diff,
            'games': games,
            'total_playtime': total_playtime
        }
        return context
    else:
        context = {
            'today': date.today(),
            'can_detach': True,
            'games': games,
            'total_playtime': total_playtime,
        }
        return context


def reset_update_url(request, user):
    can_reset = request.GET.get('reset_url')
    if can_reset:
        user.last_update_url = user.last_update_url - timedelta(hours=10)
        user.save()

def get_fullinfo_user(steam_id):
    if check_game_on_account(steam_id):
        get_stats_in_game(steam_id)
    get_friends(steam_id)
    get_recently_games(steam_id)
    try:
        GameUser.objects.update_or_create(
            user_steam_id=steam_id,
            games=games_user(steam_id)
        )
    except KeyError:
        pass
