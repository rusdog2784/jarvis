"""
Unit tests for: app/actions/weather/weather.py
"""
import pytest
from pytest_mock import mocker
from app.actions.weather.weather import Weather
from .helpful_mock_values import MockOWMObject


# Setup fixtures.
@pytest.fixture
def weather_object(mocker):
    """Returns a Weather object."""
    mocker.patch("app.actions.weather.weather.OWM", return_value=MockOWMObject("API KEY?"))
    return Weather("Hoboken")


# Weather.__init__(self, place)
def test_weather_initializer(weather_object):
    assert weather_object.one_call
    

# Weather.get_coordinates_from_place(self, place)
def test_weather_get_coordinates_from_place(weather_object):
    expected = {
        "latitude": 40.7433066,
        "longitude": -74.0323752
    }
    actual = weather_object._get_coordinates_from_place("Hoboken")
    assert actual == expected
