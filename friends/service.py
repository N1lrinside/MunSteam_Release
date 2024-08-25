from datetime import datetime
from games.service import get_data_from_api


def get_friends_list(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/'
    data = get_data_from_api(url, steam_id=steam_id)
    for i in data['friendslist']['friends']:
        add_friend = datetime.fromtimestamp(i['friend_since'])
        i['friend_since'] = add_friend.strftime('%Y-%m-%d %H:%M:%S')
    return sorted(data['friendslist']['friends'], key=lambda x: x['friend_since'])[:50]


def get_friend_info(steam_id):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    data = get_data_from_api(url, steam_id=steam_id)
    keys = ['communityvisibilitystate', 'profilestate', 'commentpermission', 'avatar',
            'avatarmedium', 'avatarhash', 'lastlogoff', 'personastate', 'realname',
            'primaryclanid', 'timecreated', 'personastateflags', 'loccountrycode',
            'locstatecode', 'loccityid']
    for info in data['response']['players']:
        dict_info = {k: v for k, v in info.items() if k not in keys}
        return dict_info