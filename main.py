import requests
# import time
# from pprint import pprint

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
            'extended': 1,
            'count': 5,
            'v': '5.130'
        }
        result = requests.get(url_vk, params=params)
        res = result.json()
        exit_file = {}
        for photo in res['response']['items']:
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }
            params = {"path": , "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params)
            file_json = response.json()
            href = file_json.get("href", "")
            response_load = requests.put(href, data=open(photo['sizes'][-1]['url'], 'rb'))
            response_load.raise_for_status()
            if response_load.status_code == 201:
                print("Success")



if __name__ == '__main__':
    user = User(611244575, token_ya)
    user.copy_photo()
