import requests
from datetime import datetime, timezone

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    """
    Fetch weather data for a city using the OpenWeatherMap API.
    :param city: Name of the city.
    :return: Dictionary containing weather details or error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        with open("apikey.txt", 'r') as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        return {"error": "'apikey.txt' file not found. Add your API key to this file."}

    url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(url).json()

    if response.get("main"):
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)
        feels_like = kelvin_to_celsius(response['main']['feels_like'])
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']

        sunrise = datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], tz=timezone.utc)
        sunset = datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], tz=timezone.utc)

        return {
            "city": city,
            "temperature": round(temp_celsius, 2),
            "feels_like": round(feels_like, 2),
            "humidity": humidity,
            "condition": description,
            "sunrise": sunrise.isoformat(),
            "sunset": sunset.isoformat(),
        }
    else:
        return {"error": "City not found or API call failed!"}
