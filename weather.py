# Weather Application
import requests
import os
from typing import Dict, Any

# Constants
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'  # Use metric units for Celsius


def fetch_weather_data(city: str) -> Dict[str, Any]:
    """Fetch weather data for a given city from the OpenWeather API."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': UNITS
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Failed to fetch weather data: {e}')


def display_weather(data: Dict[str, Any], city: str) -> None:
    """Display weather information from the API response."""
    try:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f'Weather in {city}: {weather}')
        print(f'Temperature: {temp}°C')
    except KeyError as e:
        raise KeyError(f'Invalid response format: Missing key {e}')


def main() -> None:
    """Main function to fetch and display weather data."""
    city = input('Enter city name: ').strip()
    if not city:
        print('Error: City name cannot be empty.')
        return

    try:
        weather_data = fetch_weather_data(city)
        if weather_data.get('cod') != 200:
            print(f'Error: {weather_data.get("message", "Unknown error")}')
            return
        display_weather(weather_data, city)
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
