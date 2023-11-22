import requests


def open_gist_file(url):
    """
    Открывает файл с GitHub Gist по указанному URL и возвращает его содержимое.
    :param url: URL-адрес файла на GitHub Gist.
    :return: Содержимое файла.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка при загрузке файла: {response.status_code}")
