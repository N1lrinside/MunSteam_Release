from datetime import datetime

from friends.models import UserFriends
from games.service import get_data_from_api


def get_friends_list(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/'
    data = get_data_from_api(url, steam_id=steam_id)
    try:
        for i in data['friendslist']['friends']:
            add_friend = datetime.fromtimestamp(i['friend_since'])
            i['friend_since'] = add_friend.strftime('%Y-%m-%d %H:%M:%S')
        return sorted(data['friendslist']['friends'], key=lambda x: x['friend_since'])[:50]
    except KeyError:
        return []


def get_friend_info(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    data = get_data_from_api(url, steam_id=steam_id)
    keys = ['communityvisibilitystate', 'profilestate', 'commentpermission', 'avatar',
            'avatarmedium', 'avatarhash', 'lastlogoff', 'personastate', 'realname',
            'primaryclanid', 'timecreated', 'personastateflags', 'loccountrycode',
            'locstatecode', 'loccityid']
    for info in data['response']['players']:
        return {k: v for k, v in info.items() if k not in keys}


def get_friends(steam_id):
    data = get_friends_list(steam_id)
    info_friends = []
    if data:  # Если есть друзья
        for i in data:
            info_friend = get_friend_info(i['steamid'])
            info_friend.update({'friend_since': i['friend_since']})
            info_friends.append(info_friend)
        UserFriends.objects.update_or_create(
            steam_id_user=steam_id,
            defaults={
                'friends_info': info_friends,
            }
        )


def get_info_friends(steam_id):
    data = get_friends_list(steam_id)
    if data:
        info_friend = UserFriends.objects.filter(steam_id_user=steam_id).get()
        text = 'Друзья получены'
    else:
        info_friend = []
        text = 'У вас нет друзей/Не удалось получить друзей(возможно они скрыты у вас)'
    return info_friend, text
