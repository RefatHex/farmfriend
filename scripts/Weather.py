import requests
from datetime import datetime, timedelta

api="30752aa39bddf84b696b9d7893e42335"

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    :param kelvin: Temperature in Kelvin.
    :return: Temperature in Celsius.
    """
    return kelvin - 273.15

def get_weather(city):
    """
    Fetch weather data for a city using the OpenWeatherMap API.
    :param city: Name of the city.
    :return: Dictionary containing weather details or error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    if not api:
        return {"error": "API key is missing. Define it in the 'apikey.py' file as 'api = \"your_api_key\"'."}

    url = f"{base_url}appid={api}&q={city}"
    response = requests.get(url).json()

    if response.get("main"):
        try:
            temp_kelvin = response['main']['temp']
            temp_celsius = kelvin_to_celsius(temp_kelvin)
            feels_like = kelvin_to_celsius(response['main']['feels_like'])
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']

            timezone_offset = response['timezone']  # Offset in seconds
            sunrise = datetime.utcfromtimestamp(response['sys']['sunrise'] + timezone_offset)
            sunset = datetime.utcfromtimestamp(response['sys']['sunset'] + timezone_offset)

            return {
                "city": city,
                "temperature": round(temp_celsius, 2),
                "feels_like": round(feels_like, 2),
                "humidity": humidity,
                "condition": description,
                "sunrise": sunrise.isoformat(),
                "sunset": sunset.isoformat(),
            }
        except KeyError as e:
            return {"error": f"Unexpected response structure: Missing key {str(e)}"}
    else:
        return {"error": response.get("message", "City not found or API call failed!")}
