"""
Contains the parent class for used for fetching weather information by utilizing 
the PyOWM package (OpenWeathermap API wrapper).

    - PyOWM Documentation: https://github.com/csparpa/pyowm
"""

import os
from pyowm import OWM
from geopy.geocoders import Nominatim


class Weather(object):

    def __init__(self, place: str):
        """
        Initializer. First have to fetch the coordinates using the geopy package. Then 
        use those coordinates to get the one_call object from PyOWM that should be used
        by the sub classes.

        :param place: The place to query weather data for.
        """
        api_key = os.getenv("OPEN_WEATHER_API_KEY", "NO OPEN WEATHER API KEY FOUND")
        owm = OWM(api_key=api_key)
        weather_manager = owm.weather_manager()

        coordinates = self.get_coordinates_from_place(place)
        latitude = coordinates.get("latitude")
        longitude = coordinates.get("longitude")
        
        self.one_call = weather_manager.one_call(lat=latitude, lon=longitude)

    def get_coordinates_from_place(self, place: str) -> dict:
        """
        Returns the latitude and longitude of the place provided.

        :return: Dictionary containing a latitude and longitude.
        """
        geolocator = Nominatim(user_agent="jarvis")
        location = geolocator.geocode(place)
        return {
            "latitude": location.latitude,
            "longitude": location.longitude
        }
