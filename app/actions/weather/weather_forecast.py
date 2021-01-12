"""
Sub-class of Weather. This class is strictly responsible for fetching the weather 
forecast information using PyOWM.
"""

from app.actions.weather.weather import Weather


class WeatherForecast(Weather):

    temp_metric = "fahrenheit"   # | celsius | kelvin

    def __init__(self, place: str, day: str = "today"):
        """
        Initializer.

        :param place: The place to query weather data for.
        :param interval: The interval to get the forecast for (could be 
            "today", "tomorrow", or any day of the week).
        """
        super().__init__(place=place)
        
