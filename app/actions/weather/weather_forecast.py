"""
Sub-class of Weather. This class is strictly responsible for fetching the weather 
forecast information using PyOWM.
"""

from datetime import date
from app.actions.weather.weather import Weather


class WeatherForecast(Weather):

    temp_metric = "fahrenheit"   # | celsius | kelvin
    days_of_week_map = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    def __init__(self, place: str, day: str = "today"):
        """
        Initializer.

        :param place: The place to query weather data for.
        :param interval: The interval to get the forecast for (could be 
            "today", "tomorrow", or any day of the week).
        """
        super().__init__(place=place)
        forecasts = self.one_call.forecast_daily    # returns a list of daily forecasts for the week
        self.forecast = self._get_forecast_for_interval(forecasts, interval)
        
    @staticmethod
    def _get_forecast_for_interval(forecasts: list, interval: str) -> object:
        """Returns a single Weather object out of the 8 Weather objects that are within
        the OWM one_call forecast_daily list. The single object returned is determined
        by an algorithm that allows the end user to simply provide a string interval ('today', 
        'tomorrow', 'Monday', 'Tuesday', etc.) then fetch the correct forecast object.

        Args:
            forecasts (list): List of Weather objects. Each is a daily forecast.
            interval (str): The user provided, relative time for which forecast to fetch 
                ('today', 'tomorrow', 'Monday', 'Tuesday', etc.).

        Returns:
            object: A PyOWM Weather object.
        """
        interval = interval.lower()
        if interval == "today":
            difference = 0
        elif interval == "tomorrow":
            difference = 1
        else:
            today = date.today().weekday()
            future = self.days_of_week_map.get(interval)
            difference = future - today
            if difference < 0:
                difference = today + abs(difference) + 1
            return forecasts[difference]
        
    def get_weather_report(self) -> str:
        """Returns a small description of the forecasted weather.
        
        Returns:
            str: A small description of the forecasted weather.
        """
        
