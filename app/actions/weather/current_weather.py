"""
Sub-class of Weather. This class is strictly responsible for fetching current weather 
information using PyOWM.
"""

from app.actions.weather.weather import Weather


class CurrentWeather(Weather):

    temp_metric = "fahrenheit"   # | celsius | kelvin
    
    def __init__(self, place: str):
        """Initializer.

        Args:
            place (str): The place to query weather data for.
        """
        super().__init__(place=place)
        self.current_weather = self.one_call.current

    def get_weather_report(self) -> str:
        """Returns a small description of the current weather.

        Returns:
            str: A small description of the current weather.
        """
        return self.current_weather.detailed_status

    def get_temperature(self) -> float:
        """Returns the current temperature in fahrenheit.
        
        Returns: 
            float: Temperature in fahrenheit.
        """
        temperature = self.current_weather.temperature(self.temp_metric)
        return temperature.get("temp")

    def get_feels_like_temperature(self) -> float:
        """Returns the current "feels like" temperature in fahrenheit.
        
        Returns:
            float: Temperature in fahrenheit.
        """
        temperature = self.current_weather.temperature(self.temp_metric)
        return temperature.get("feels_like")
