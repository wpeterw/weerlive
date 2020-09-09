import requests
from collections import namedtuple
from .descriptions import Descriptions


class WeerLive:
    def __init__(self, api_key, location):
        api_key = api_key
        location = location
        self.descriptions = Descriptions()
        self.url = f"http://weerlive.nl/api/json-data-10min.php?key={api_key}&locatie={location}"

    def get_weather_data(self):

        return requests.get(url=self.url).json()["liveweer"][0]

    def get_descriptions(self, weather_data, descriptions):

        return dict((descriptions[key], value) for (key, value) in weather_data.items())

    def dict_to_tuple(self, weather_dict):

        return namedtuple("weather_data", weather_dict.keys())(*weather_dict.values())

    def get_live_weather(self):

        weather = self.get_weather_data()
        weather_with_descriptions = self.get_descriptions(
            weather_data=weather, descriptions=self.descriptions.descriptions_dict()
        )

        return self.dict_to_tuple(weather_with_descriptions)
