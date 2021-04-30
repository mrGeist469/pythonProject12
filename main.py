import requests
from pprint import pprint


with open('token.txt', encoding='utf-8') as f:
    token_vk = f.readline().strip()
    token_ya = f.readline().strip()


class User:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def copy_photo(self):
        url_vk = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': token_vk,
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extend': 1,
            'count': 6,
            'v': 5.130
        }
        result = requests.get(url_vk, params=params)


