import requests
import os
from googleapiclient.discovery import build
import json

import isodate

api_key: str = 'YT_API_KEY'
youtube: str = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, channel_name: str, channel_description: str, channel_url, count_follower: int,
                 count_video: int, see_all: int) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = None
        self.channel_name = channel_name
        self.channel_description = channel_description
        self.channel_url = channel_url
        self.count_follower = count_follower
        self.count_video = count_video
        self.see_all = see_all

    # def printj(self, dict_to_print: dict) -> None:
    #     """Выводит словарь в json-подобном удобном формате с отступами"""
    #     print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
        payload = {}
        headers = youtube
        response = requests.request("GET", url, headers=headers, data=payload)

        return response.text

    def to_json(self, response):

        print(json.dumps(response, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        return dict_channel
