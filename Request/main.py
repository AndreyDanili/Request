from pprint import pprint
import requests


def heroes_info(name):
    heroes_info = {}
    heroes_power = {}
    for heroes_name in name:
        url = f'https://superheroapi.com/api/2619421814940190/search/{heroes_name}'
        response = requests.get(url)
        heroes_info[heroes_name] = response.json()['results']
        for characteristic in heroes_info[heroes_name]:
            if heroes_name == characteristic['name']:
                heroes_power[heroes_name] = int(characteristic['powerstats']['intelligence'])
    win_heroes = max(heroes_power, key=heroes_power.get)
    pprint(win_heroes)


heroes_info(['Hulk', 'Captain America', 'Thanos'])
