import os
import requests
from concurrent.futures import ThreadPoolExecutor


images = [
    'https://cdn.pixabay.com/photo/2019/10/27/18/48/chinatown-4582511_960_720.jpg',
    'https://cdn.pixabay.com/photo/2019/11/12/15/47/aesthetic-4621334_960_720.jpg',
    'https://cdn.pixabay.com/photo/2019/10/07/11/26/wintry-4532412_960_720.jpg'
]


def download(url):
    filename = os.path.basename(url)
    name = url.split('/')[9]
    req = requests.get(url).content

    with open(name, 'wb') as file:
        file.write(req)
        print(f'{name} was downloaded!').format(filename)


with ThreadPoolExecutor(max_workers=1) as exec:
    exec.map(download, images)
