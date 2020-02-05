import requests
import os
import json


class SheepApi:
    def __init__(self):
        self.base_url = 'https://stickntrack.sensolus.com:443/rest/api/v1/devices'
        self.gps_locations_path = '/{serial}/gpslocations'
        self.api_key = os.getenv('SENSOLUS_API_KEY')

    def __call_api(self):
        response = requests.get(self.base_url, params={'apiKey': self.api_key})
        devices = response.json()
        print(devices)
        serial_numbers = [x['serial'] for x in devices]
        output = dict()
        for serial_number in serial_numbers:
            response = requests.get(self.base_url + self.gps_locations_path.format(serial=serial_number),
                                    params={'apiKey': self.api_key, 'from': 'last_hour'})
            output[serial_number] = response.json()
        return output

    def get_sheep_str(self) -> str:
        response = self.__call_api()
        return json.dumps(response)

    def get_sheep_dict(self) -> dict:
        response = self.__call_api()
        return response
