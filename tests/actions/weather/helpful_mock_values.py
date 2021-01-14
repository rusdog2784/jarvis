"""
Contains any and all mock classes and functions that might be found useful in 
the testing of the weather action functionalities.
"""
from unittest.mock import MagicMock


def mock_temperature_function(metric: str = "fahrenheit"):
    return {
        "temp": 69.420,
        "feels_like": 96.420
    }


class MockOneCallObject(object):
    def __init__(self):
        self.current = MagicMock(
            detailed_status="slightly cloudy",
            temperature=mock_temperature_function
        )
        self.forecast_daily = MagicMock()


class MockWeatherManagerObject(object):
    def one_call(self, lat, lon):
        return MockOneCallObject()


class MockOWMObject(object):
    def __init__(self, api_key):
        print("Mocking the PyOWM OWM class to avoid increasing API limits.")
        
    def weather_manager(self):
        return MockWeatherManagerObject()
    
    
class MockWeatherClass(object):
    def __init__(self, place):
        self.one_call = MockOneCallObject()
