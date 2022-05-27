import requests


class VkClass:
    token = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
    url = 'https://api.vk.com/method/'

    def __init__(self, token: str, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def photo_get(self, owner_id: str):
        photo_get_params = {
            'access_token': VkClass.token,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': '1',
            'v': '5.131'
        }
        url = self.url + 'photos.get?'
        return requests.get(url, params={**self.params, **photo_get_params}).json()
