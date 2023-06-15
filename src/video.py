import os
import requests


class Video:
    def __init__(self, id_video, name_video, url_video, count_see, count_like):
        self.id_video = id_video
        self.name_video = name_video
        self.url_video = url_video
        self.count_see = count_see
        self.count_like = count_like


class PLVideo:
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, id_video, id_play):
        self.id_video = id_video
        self.id_play = id_play


