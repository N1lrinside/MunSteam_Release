from django.conf import settings

from games.service import get_data_from_api

api_key = settings.API_KEY


def games_user(steam_id):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    data = get_data_from_api(url, steam_id=steam_id)
    list_games = []
    for i in data['response']['games']:
        if i['playtime_forever'] // 60 > 0:
            list_games.append([i['name'], i['appid'], i['playtime_forever'] // 60])
    return {i[1]: i[0] for i in sorted(list_games, key=lambda x: x[2], reverse=True)[:16]}


def get_achiviements_game(steam_id, app_id=578080):
    url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?l=russian"
    data = get_data_from_api(url, app_id, steam_id)
    if data['playerstats']['success']:
        try:
            info = data['playerstats']['achievements']
            filtered_achievements = [
                {
                    'achieved': achievement['achieved'],
                    'name': achievement.get('name', 'No Name'),
                    'description': achievement.get('description', 'No Description')
                }
                for achievement in info
            ]
            return filtered_achievements
        except KeyError:
            return False
    else:
        return False
