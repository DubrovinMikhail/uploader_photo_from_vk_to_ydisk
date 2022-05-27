import vk
import yadisk
import json
from tqdm import tqdm

TOKEN_YANDEX = yadisk.YaUploader.token
TOKEN_VK = vk.VkClass.token
uploader = yadisk.YaUploader(TOKEN_YANDEX)
vk_client = vk.VkClass(TOKEN_VK, '5.131')
info = 'info.json'

if __name__ == '__main__':
    vk_id = '552934290'
    date_photo = vk_client.photo_get(vk_id)['response']['items']
    name_photo_dict = {}
    photo_list = []

    for photo in date_photo:
        name_photo_dict[photo['likes']['count']] = max(photo['sizes'], key=lambda s: s['width'] * ['height'])['url']
        photo_list.append({"file_name": f"{photo['likes']['count']}.jpg", 'size': photo['sizes'][-1]['type']})
    uploader.dir_inst(vk_id)
    with open(info, 'w') as outfile:
        json.dump(photo_list,outfile)
    for key, value in tqdm(name_photo_dict.items()):
        uploader.upload(f'{vk_id}/{key}', value)
