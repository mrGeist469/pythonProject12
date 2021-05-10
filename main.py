import requests
import time
from tqdm import tqdm
import json


class User:
    def __init__(self, user_id, vk, ya):
        self.user_id = user_id
        self.token_vk = vk
        self.token_ya = ya

    def copy_photo(self):
        url_vk = 'https://api.vk.com/method/photos.get'
        params_vk = {
            'access_token': self.token_vk,
            'owner_id': self.user_id,
            'album_id': 'profile',
            'extended': 1,
            'count': 5,
            'v': '5.130'
        }
        result = requests.get(url_vk, params=params_vk)
        time.sleep(1)
        res = result.json()
        time.sleep(1)
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_ya)
        }
        params = {'path': '/Photo VK'}
        requests.put(upload_url, headers=headers, params=params)
        exit_file = []
        file_name = []
        print('Start copying photo')
        time.sleep(1)
        for photo in tqdm(res['response']['items'], desc="Copying"):
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token_ya)
            }
            if photo['likes']['count'] not in file_name:
                params = {'path': f"/Photo VK/{str(photo['likes']['count'])}.jpg",
                          'url': photo['sizes'][-1]['url']
                          }
                requests.post(upload_url, headers=headers, params=params)
                exit_file.extend(json.dumps({'file_name': f"{str(photo['likes']['count'])}.jpg",
                                             'size': photo['sizes'][-1]['type']}, indent=4).split("'"))
                file_name.append(photo['likes']['count'])
                time.sleep(1)
            else:
                params = {
                    'url': photo['sizes'][-1]['url'],
                    'path': f"/Photo VK/{str(photo['likes']['count'])}_{str(photo['date'])}.jpg"
                }
                requests.post(upload_url, headers=headers, params=params)
                exit_file.extend(json.dumps({'file_name': f"{str(photo['likes']['count'])}_{str(photo['date'])}.jpg",
                                             'size': photo['sizes'][-1]['type']}, indent=4).split("'"))
                file_name.append(str(photo['likes']['count']) + "_" + str(photo['date']))
                time.sleep(1)
        print('Finished')
        with open('file.json', 'w') as file:
            json.dump(exit_file, file)


with open('token.txt', encoding='utf-8') as f:
    token_vk = f.readline().strip()
    token_ya = f.readline().strip()

if __name__ == '__main__':
    user = User(611244575, token_vk, token_ya)
    user.copy_photo()
