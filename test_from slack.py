class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photos(self, vk_id):

        # Получение фотографии с профиля с использованием метода photos.get

        photos_get_url = self.url + 'photos.get'

        params = {
            'owner_id' : vk_id,
            'album_id' : 'profile',
            'rev' : 0,
            'extended' : 1,
            'photo_sizes' : 0,
            'count' : 20
        }

        res = requests.get(photos_get_url, params={**self.params, **params}).json()

        return res['response']['items']
Вот что я получаю :
[{'album_id': -6,
  'can_comment': 1,
  'comments': {'count': 2},
  'date': 1562944607,
  'has_tags': False,
  'id': 457239018,
  'likes': {'count': 17, 'user_likes': 1},
  'owner_id': 552934290,
  'post_id': 1,
  'reposts': {'count': 0},
  'sizes': [{'height': 130,
             'type': 'm',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/sPtke3HEZH4N0qpdrjtD_YfLr0ZfEJ4G5W-GHF-gRMTTgJ2s1au_WBIaJQY_xfgEUnl3fiGj.jpg?size=130x130&quality=96&type=album',
             'width': 130},
            {'height': 130,
             'type': 'o',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/sPtke3HEZH4N0qpdrjtD_YfLr0ZfEJ4G5W-GHF-gRMTTgJ2s1au_WBIaJQY_xfgEUnl3fiGj.jpg?size=130x130&quality=96&type=album',
             'width': 130},
            {'height': 200,
             'type': 'p',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/vFzvg97YsENgEeiKh4x6UwQLW7jFO-JGRE397T0tsVp32c-EbXWwcFVkaw6QEPqds5GKRQSN.jpg?size=200x200&quality=96&type=album',
             'width': 200},
            {'height': 320,
             'type': 'q',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/KTTtg5DnD39esdAXDbCnLMROseX4VoZzXcG9ZF8ILVZKlHf9gGhjP2YpAlP_HZGtIaT5ZVPi.jpg?size=320x320&quality=96&type=album',
             'width': 320},
            {'height': 400,
             'type': 'r',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/Ewp6frruZjG76BgnZ74s9Zu0stqInLHNRbTrp0REiXLRZEq8qcZtSwXNjciM8WEEgPCUgiwM.jpg?size=400x400&quality=96&type=album',
             'width': 400},
            {'height': 75,
             'type': 's',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/v0EYlkR85w6UiE0gY5nurlWH4wNih1cCD8a-8rx0YwNIFyNk7ZEvPuHuTzO84ioRHMdOX8Sm.jpg?size=75x75&quality=96&type=album',
             'width': 75},
            {'height': 400,
             'type': 'x',
             'url': 'https://sun9-28.userapi.com/s/v1/if1/Ewp6frruZjG76BgnZ74s9Zu0stqInLHNRbTrp0REiXLRZEq8qcZtSwXNjciM8WEEgPCUgiwM.jpg?size=400x400&quality=96&type=album',
             'width': 400}],
  'tags': {'count': 0},
  'text': ''}