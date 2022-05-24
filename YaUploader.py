from pprint import pprint

import requests

from yandexdisk1 import YaUpload

import os

token_yd = os.getenv("TOKEN_YD")
print(token_yd)

YANDEX_TOKEN = token_yd

if __name__ == '__main__':
    yadisk = YaUpload(YANDEX_TOKEN)
    print(yadisk.get_link('/'))
    print(yadisk._get_upload_link('/tmp/'))
