import requests


def open_gist_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка при загрузке файла: {response.status_code}")
