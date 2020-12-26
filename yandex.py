import requests

YA_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def create_folder(folder_name):
    response = requests.put(
        'https://cloud-api.yandex.net/v1/disk/resources',
        params={'path': folder_name},
        headers={'Authorization': f'OAuth {YA_TOKEN}'},
    )
    return response


def check_folder(folder_path):
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                            params={'path': folder_path},
                            headers={'Authorization': f'OAuth {YA_TOKEN}'})
    items = response.json()['_embedded']['items']
    items_names = []
    for item in items:
        name = item['name']
        items_names.append(name)
    return items_names


if __name__ == '__main__':
    create_folder(input('Введите название новой папки: '))
    check_folder('disk:/')
