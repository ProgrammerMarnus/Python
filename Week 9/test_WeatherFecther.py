import pytest
from WeatherClient import WeatherFetcher
import json

with open("settings.json", "r") as json_file:
    s = json.load(json_file)
    global WEATHER_FETCHER 
    WEATHER_FETCHER = WeatherFetcher(s["Settings"])

def test_get_coordinates_valid_city():
    
    city = "Johannesburg"
    expected_coordinates = (-26.2041, 28.0456)
    assert WEATHER_FETCHER.get_coordinates(city) == expected_coordinates

def test_get_coordinates_invalid_city():
    city = "InvalidCity"
    assert WEATHER_FETCHER.get_coordinates(city) is None

def test_fetch_weather_valid_coordinates():
    lat, lon = -26.2041, 28.0456  # Johannesburg coordinates
    weather_data = WEATHER_FETCHER.fetch_weather(lat, lon)
    assert weather_data is not None
    assert 'temperature' in weather_data
    assert 'windspeed' in weather_data
    assert 'winddirection' in weather_data
    assert 'weathercode' in weather_data

def test_fetch_weather_invalid_coordinates():
    lat, lon = 999, 999  # Invalid coordinates
    weather_data = WEATHER_FETCHER.fetch_weather(lat, lon)
    assert weather_data is None

def test_format_weather_data_valid_data():
    weather_data = {
        'temperature': 25,
        'windspeed': 5,
        'winddirection': 180,
        'weathercode': 0
    }
    formatted_data = WEATHER_FETCHER.format_weather_data(weather_data)
    assert formatted_data is None 

def test_format_weather_data_invalid_data():
    weather_data = None
    formatted_data = WEATHER_FETCHER.format_weather_data(weather_data)
    assert formatted_data is None

def test_update_settings():
    new_settings = {"Temperature_Measurement": "F"}
    WEATHER_FETCHER.update_settings(new_settings)
    assert WEATHER_FETCHER.settings["Temperature_Measurement"] == "F"