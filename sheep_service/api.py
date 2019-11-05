import requests
import os


class SheepApi:
    def __init__(self):
        self.url = 'https://stickntrack.sensolus.com:443/rest/api/v1/devices'
        self.api_key = os.getenv('SENSOLUS_API_KEY')

    def __call_api(self):
        return requests.get(self.url, params={'apiKey': self.api_key})

    def get_sheep_str(self) -> str:
        response = self.__call_api()
        return response.text

    def get_sheep_dict(self) -> dict:
        response = self.__call_api()
        return response.json()
