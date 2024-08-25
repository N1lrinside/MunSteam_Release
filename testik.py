import requests
import os
from datetime import datetime

api_key = os.environ.get('STEAM_API')


def get_friend_info(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    params = {
        'key': 'A841CD672B51AB7D6C82A7CDA8B28E86',
        'steamids': steam_id
    }
    response = requests.get(url, params=params)
    data = response.json()
    keys = ['communityvisibilitystate', 'profilestate', 'commentpermission', 'avatar',
            'avatarmedium', 'avatarhash', 'lastlogoff', 'personastate', 'realname',
            'primaryclanid', 'timecreated', 'personastateflags', 'loccountrycode',
            'locstatecode', 'loccityid']
    for info in data['response']['players']:
        dict_info = {k: v for k, v in info.items() if k not in keys}
        return dict_info


def get_friends_list(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/'
    params = {
        'key': 'A841CD672B51AB7D6C82A7CDA8B28E86',
        'steamid': steam_id,
        'relationship': 'friend',
    }
    response = requests.get(url, params=params)
    data = response.json()
    for i in data['friendslist']['friends']:
        i['friend_since'] = datetime.fromtimestamp(i['friend_since'])
    return sorted(data['friendslist']['friends'], key=lambda x: x['friend_since'])[:50]


l = get_friends_list(76561199764676485)
print(bool(l))


# У вас нет друзей, не привязан аккаунт, не вошли