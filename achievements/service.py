from achievements.models import GameAchievement
from games.service import get_data_from_api


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


def get_achievements(steam_id, app_id):
    if exists_achievements(steam_id, app_id):
        achievements, count_achievements, count_achieved, percentage = exists_achievements(steam_id, app_id)
    else:
        achievements = get_achiviements_game(steam_id, app_id)
        count_achievements = len(achievements)
        count_achieved = len([i for i in achievements if i['achieved']])
        percentage = (count_achieved / count_achievements) * 100
        GameAchievement.objects.update_or_create(
                user_steam_id=steam_id,
                app_id=app_id,
                achievements=achievements
        )
    return achievements, count_achievements, count_achieved, percentage


def exists_achievements(steam_id, app_id):
    achiv_exists = GameAchievement.objects.filter(user_steam_id=steam_id, app_id=app_id)
    if achiv_exists.exists():
        achievements = achiv_exists.first().achievements
        count_achievements = len(achievements)
        count_achieved = len([i for i in achievements if i['achieved']])
        percentage = (count_achieved / count_achievements) * 100
        return [achievements, count_achievements, count_achieved, percentage]