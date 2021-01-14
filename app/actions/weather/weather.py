"""
Contains the parent class for used for fetching weather information by utilizing 
the PyOWM package (OpenWeathermap API wrapper).

    - PyOWM Documentation: https://github.com/csparpa/pyowm
"""

import os
from pyowm import OWM
from geopy.geocoders import Nominatim


class Weather(object):
    
    def __init__(self, place: str) -> None:
        """Initializer. First have to fetch the coordinates using the geopy package. Then 
        use those coordinates to get the one_call object from PyOWM that should be used
        by the sub classes.

        Args:
            place (str): The place to query weather data for.
        """
        api_key = os.getenv("OPEN_WEATHER_API_KEY", "NO OPEN WEATHER API KEY FOUND")
        owm = OWM(api_key=api_key)
        weather_manager = owm.weather_manager()

        coordinates = self._get_coordinates_from_place(place)
        latitude = coordinates.get("latitude")
        longitude = coordinates.get("longitude")
        
        self.one_call = weather_manager.one_call(lat=latitude, lon=longitude)
        
    @staticmethod
    def _get_coordinates_from_place(place: str) -> dict:
        """Returns the latitude and longitude of the place provided.

        Args:
            place (str): The place to get coordinates for.

        Returns:
            dict: Dictionary containing the place's latitude and longitude.
        """
        geolocator = Nominatim(user_agent="jarvis")
        location = geolocator.geocode(place)
        return {
            "latitude": location.latitude,
            "longitude": location.longitude
        }
