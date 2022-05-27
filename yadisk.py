import requests


class YaUploader:
    token = ""
    host = "https://cloud-api.yandex.net:443"
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}

    def __init__(self, token: str):
        self.token = token

    def dir_inst(self, name):
        url = f'{self.host}/v1/disk/resources'
        params = {'path': name}
        requests.put(url, params=params, headers=YaUploader.headers)

    def upload(self, path: str, link: str):
        url = f'{self.host}/v1/disk/resources/upload/'
        params = {'path': path, 'url': link}
        requests.post(url, params=params, headers=YaUploader.headers)
