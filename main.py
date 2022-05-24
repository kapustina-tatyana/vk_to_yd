import time


import json
import os
from vkphoto import VkPhoto
from yadisk import YaDisk
import datetime


token_yd = os.getenv("TOKEN_YD")
#print(token_yd)

token_vk = os.getenv("TOKEN_VK")
# print(token_vk)

yadisk = YaDisk(token_yd)
vkphoto = VkPhoto(token_vk)


def PhotoDoUpLoader(path, count=5):
    """ Загрузка фотографий из vk в папку на Яндекс диске."""
    downloadFiles = vkphoto.PhotosGetAllParams(552934290)

    downloadFilesSort = sorted(downloadFiles, key=lambda x: x['likes'], reverse=True)
    basenamePrev = 0
    for i in range(0, count):
        basename = downloadFilesSort[i]['likes']
        url = downloadFilesSort[i]['url']
        # print(basename)
        if basename == basenamePrev:
            dateForName = downloadFilesSort[i]['date']
            readableTime = datetime.datetime.fromtimestamp(dateForName).strftime('%d%m%Y')
            fileName = f"{path}/{basename}_{readableTime}.jpg"
            print(fileName)
            yadisk.upload_link(fileName, url)
        else:
            fileName = f"{path}/{basename}.jpg"
            print(fileName)
            basenamePrev = basename
            yadisk.upload_link(fileName, url)
        i += i
        time.sleep(3)


def PhotoLoad(path, count=5):
    yadisk.create_folder(path)
    PhotoDoUpLoader(path)

if __name__ == '__main__':
    # PhotoLoad('/folder_for_photo',3)

    vkphoto.PhotosGetAllTest(552934290)


    # PhotoDoUpLoader()
    # vkphoto.PhotosGetAllParams(552934290)

    # yadisk.upload_link('/123.jpg', 'https://sun9-28.userapi.com/s/v1/if1/Ewp6frruZjG76BgnZ74s9Zu0stqInLHNRbTrp0REiXLRZEq8qcZtSwXNjciM8WEEgPCUgiwM.jpg?size=400x400&quality=96&type=album')
