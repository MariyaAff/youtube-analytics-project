import requests
import os
from googleapiclient.discovery import build
import json

import isodate


# api_key: str = 'YT_API_KEY'
# youtube: str = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube: str = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id: str = channel_id
        self.channel = None
        # self.dict_of_channel = self.get_service().channels().list(id=self.channel_id,
        #
        #                                                           part='snippet,statistics').execute()  # id канала
        #
        # self.title = self.dict_of_channel.get('items')[0].get('snippet').get('title')  # название канала
        #
        # self.description = self.dict_of_channel.get('items')[0].get('snippet').get('description')  # описание канала
        #
        # self.url = f"https://www.youtube.com/channel/{self.channel_id}"  # ссылка на канал
        #
        # self.count_follower = int(self.dict_of_channel.get('items')[0].get('statistics').get(
        #
        #     'subscriberCount'))  # количество подписчиков
        #
        # self.video_count = int(
        #     self.dict_of_channel.get('items')[0].get('statistics').get('videoCount'))  # количество видео
        #
        # self.count_views = int(self.dict_of_channel.get('items')[0].get('statistics').get(
        #
        #     'viewCount'))  # общее количество просмотров

    # def __str__(self):
    #     return f'{self.channel_name} {self.channel_url}'

    #
    #
    # def __add__(self, other):
    #     return moscowpython + highload
    #
    # def __sub__(self, other):
    #     return moscowpython - highload
    #
    # def __gt__(self, other):
    #     if moscowpython > highload:
    #         return moscowpython
    #     return None

    # def printj(self, dict_to_print: dict) -> None:
    #     """Выводит словарь в json-подобном удобном формате с отступами"""
    #     print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    # @classmethod
    # def get_service(cls):
    #     url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
    #     payload = {}
    #     # headers = youtube
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #
    #     return response.text
    #
    # def to_json(self, response):
    #     print(json.dumps(response, indent=2, ensure_ascii=False))

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        return dict_channel


# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# highload = Channel('UCwHL6WHUarjGfUM_586me8w')
