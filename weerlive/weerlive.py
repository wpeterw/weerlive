import requests
from collections import namedtuple


class WeerLive:
    def __init__(self, api_key, location):
        api_key = api_key
        location = location
        self.url = f"http://weerlive.nl/api/json-data-10min.php?key={api_key}&locatie={location}"

    def get_weather_data(self):

        return requests.get(url=self.url).json()["liveweer"][0]

    def descriptions_dict(self):

        descriptions = {
            "plaats": "location",
            "temp": "current_temperature",
            "gtemp": "temperature_feels_like",
            "samenv": "description_weather_condition",
            "lv": "relative_humidity",
            "windr": "wind_direction",
            "windms": "wind_speed_ms",
            "winds": "wind_speed_beaufort",
            "windk": "wind_speed_in_knots",
            "windkmh": "wind_speed_in_kmh",
            "luchtd": "barometric_pressure",
            "ldmmhg": "barometric_pressure_in_mm_hg",
            "dauwp": "dewpoint",
            "zicht": "visibility_in_km",
            "verw": "short_dayforecast",
            "sup": "sunrise",
            "sunder": "sunset",
            "image": "image_name",
            "d0weer": "weather_icon_today",
            "d0tmax": "maxtemp_today",
            "d0tmin": "mintemp_today",
            "d0windk": "wind_speed_today_bft",
            "d0windknp": "wind_speed_today_knp",
            "d0windms": "wind_speed_today_ms",
            "d0windkmh": "wind_speed_today_kmh",
            "d0windr": "wind_direction_today",
            "d0neerslag": "probability_of_precipitation_today_percent",
            "d0zon": "sun_chance_today_percent",
            "d1weer": "weather_icon_tomorrow",
            "d1tmax": "maxtemp_tomorrow",
            "d1tmin": "mintemp_tomorrow",
            "d1windk": "wind_speed_tomorrow_bft",
            "d1windr": "wind_direction_tomorrow",
            "d1windknp": "wind_speed_tomorrow_knp",
            "d1windms": "wind_speed_tomorrow_ms",
            "d1windkmh": "wind_speed_tomorrow_kmh",
            "d1neerslag": "probability_of_precipitation_tomorrow_percent",
            "d1zon": "sun_chance_tomorrow_percent",
            "d2tmax": "maxtemp_day_after_tomorrow",
            "d2tmin": "mintemp_day_after_tomorrow",
            "d2weer": "weather_icon_day_after_tomorrow",
            "d2windk": "wind_speed_day_after_tomorrow_bft",
            "d2windr": "wind_direction_after_tomorrow",
            "d2windknp": "wind_speed_day_after_tomorrow_knp",
            "d2windms": "wind_speed_day_after_tomorrow_ms",
            "d2windkmh": "wind_speed_day_after_tomorrow_kmh",
            "d2neerslag": "probability_of_precipitation_day_after_tomorrow_percent",
            "d2zon": "sun_chance_day_after_tomorrow_percent",
            "alarm": "warning_active",
            "alarmtxt": "warning_text",
        }

        return descriptions

    def correct_descriptions(self, weather_data, descriptions):

        return dict((descriptions[key], value) for (key, value) in weather_data.items())

    def dict_to_tuple(self, weather_dict):

        return namedtuple("weather_data", weather_dict.keys())(*weather_dict.values())

    def get_live_weather(self):

        weather = self.get_weather_data()
        weather_with_descriptions = self.correct_descriptions(
            weather_data=weather, descriptions=self.descriptions_dict()
        )

        return self.dict_to_tuple(weather_with_descriptions)
