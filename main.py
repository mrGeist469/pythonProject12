import requests
from pprint import pprint


with open('token.txt', encoding='utf-8') as f:
    token_vk = f.readline()
    token_ya = f.readline()


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def
