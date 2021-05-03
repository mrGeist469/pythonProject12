import requests
import time
from tqdm import tqdm
import json
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
        params_vk = {
            'access_token': token_vk,
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extended': 1,
            'count': 5,
            'v': '5.130'
        }
        result = requests.get(url_vk, params=params_vk)
        res = result.json()
        pprint(res)
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': '/Photo VK'}
        requests.put(upload_url, headers=headers, params=params)
        exit_file = []
        file_name = []
        time.sleep(1)
        for photo in tqdm(res['response']['items']):
            load_dict = {}
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }
            if f"{photo['likes']['count']}.jpg" is not file_name:
                params = {'path': f"/Photo VK/{str(photo['likes']['count'])}.jpg",
                          'url': photo['sizes'][-1]['url']
                          }
                response = requests.post(upload_url, headers=headers, params=params)
                load_dict['file_name'] = f"{str(photo['likes']['count'])}.jpg"
                load_dict['size'] = photo['sizes'][-1]['type']
                exit_file.extend(load_dict)
                file_name.extend(str(photo['likes']['count']))
                time.sleep(1)
            else:
                params = {
                    'url': photo['sizes'][-1]['url'],
                    'path': f"/Photo VK/{str(photo['likes']['count'])}_{str(photo['date'])}.jpg"
                }
                response = requests.post(pload_url, headers=headers, params=params)
                load_dict['file_name'] = f"{str(photo['likes']['count'])}_{str(photo['date'])}.jpg"
                load_dict['size'] = photo['sizes'][-1]['type']
                exit_file.extend(load_dict)
                file_name.extend(f"{str(photo['likes']['count'])}_{str(photo['date'])}")
                time.sleep(1)
        pprint(exit_file)
        print(file_name)


            # print(response.json)


if __name__ == '__main__':
    user = User(611244575, token_ya)
    user.copy_photo()
