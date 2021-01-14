"""
Unit tests for: app/actions/weather/current_weather.py
"""
import pytest
from pytest_mock import mocker
from app.actions.weather.current_weather import CurrentWeather
from .helpful_mock_values import MockWeatherClass


# Setup fixtures.
@pytest.fixture
def current_weather_object(mocker):
    """Returns a CurrentWeather object."""
    # Set the parent class to the mocked Weather class.
    CurrentWeather.__bases__ = (MockWeatherClass,)
    return CurrentWeather("Hoboken")


# CurrentWeather.__init__(self, place)
def test_initializer(current_weather_object):
    assert current_weather_object.current_weather
    
    
#CurrentWeather.get_weather_report(self)
def test_get_weather_report(current_weather_object):
    expected = "slightly cloudy"
    actual = current_weather_object.get_weather_report()
    assert actual == expected
    
    
# CurrentWeather.get_temperature(self)
def test_get_temperature(current_weather_object):
    expected = 69.420
    actual = current_weather_object.get_temperature()
    assert actual == expected
    

# CurrentWeather.get_feels_like_temperature(self)
def test_get_feels_like_temperature(current_weather_object):
    expected = 96.420
    actual = current_weather_object.get_feels_like_temperature()
    assert actual == expected
