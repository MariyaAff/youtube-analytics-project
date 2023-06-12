import requests
import os
from googleapiclient.discovery import build
import json

import isodate


class Channel:
    api_key: str = os.getenv('YT_API_KEY')
    youtube: str = build('youtube', 'v3', developerKey=api_key)

    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = None

    # def printj(self, dict_to_print: dict) -> None:
    #     """Выводит словарь в json-подобном удобном формате с отступами"""
    #     print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    # def get_service(cls):
    #     url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
    #     payload = {}
    #     headers = api_key
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #
    #     print(response.text)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        return dict_channel
