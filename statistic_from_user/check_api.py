import os
import requests
from dotenv import load_dotenv
load_dotenv()

steam_api = os.getenv('STEAM_API')
steam_url = os.getenv('STEAM_URL')
app_id = '550' # 730 - CS2, 570 - Dota 2, 578080 - PUBG
params = {
    'appid': app_id,
    'key': steam_api,
    'steamid': 76561198821788610
}

response = requests.get(steam_url, params=params)
print(response.json())
data = [i for i in response.json()['playerstats']]
data2 = [i for i in response.json()['playerstats']['stats']]
print(data, data2, sep='\n')
