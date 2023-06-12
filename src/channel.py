import requests


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    # @classmethod
    def get_service(cls):
        # url = 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
        # params = {'name': ' ', 'description': ' ', 'click': ' ', 'count_people': ' ', 'count_video': ' ', 'look': ' '}
        response = requests.get('https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A')
        print(response.text)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass
