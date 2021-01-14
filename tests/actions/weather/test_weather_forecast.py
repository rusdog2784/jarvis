"""
Unit tests for: app/actions/weather/weather_forecast.py
"""
import pytest
from pytest_mock import mocker
from app.actions.weather.weather_forecast import WeatherForecast
from .helpful_mock_values import MockWeatherClass


# Setup fixtures.
@pytest.fixture
def weather_forecast_object(mocker):
    """Returns a WeatherForecast object."""
    # Set the parent class to the mocked Weather class.
    WeatherForecast.__bases__ = (MockWeatherClass,)
    return WeatherForecast("Hoboken", "today")


# WeatherForecast.__init__(self, place, interval)
def test_initializer(current_weather_object):
    assert current_weather_object.current_weather
    
