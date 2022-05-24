from pprint import pprint

import requests

from yadisk import YaDisk

import os

token_yd = os.getenv("TOKEN_YD")
print(token_yd)

YANDEX_TOKEN = token_yd

if __name__ == '__main__':
    yadisk = YaDisk(token_yd)
    # print(yadisk.get_headers())
    # pprint(yadisk.get_files_list())
    # yadisk._get_upload_link('/17.jpg')
    # print(yadisk._get_upload_link)
    # pprint(yadisk._get_upload_link('/'))
    yadisk.upload_link('/123.jpg', 'https://sun9-28.userapi.com/s/v1/if1/Ewp6frruZjG76BgnZ74s9Zu0stqInLHNRbTrp0REiXLRZEq8qcZtSwXNjciM8WEEgPCUgiwM.jpg?size=400x400&quality=96&type=album')
