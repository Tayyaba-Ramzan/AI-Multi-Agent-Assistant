import requests
from decouple import config
from agents import function_tool

WEATHER_API_KEY = config("WEATHER_API_KEY")

@function_tool
def get_weather(city: str = "Lahore") -> str:
    """
    Retrieve the current weather conditions for a specified city using WeatherAPI.

    This tool fetches real-time weather data, including temperature in Celsius and 
    a brief description of the weather condition (e.g., sunny, cloudy, raining, etc.). 
    It uses the WeatherAPI service and returns a user-friendly weather summary.

    Example:
        >>> get_weather("Karachi")
        "In Karachi, it's 33°C and mostly sunny."

    Parameters:
        city (str, optional): The name of the city to fetch weather information for. 
                              Defaults to "Lahore".

    Returns:
        str: A formatted string with the current temperature and condition.
             If an error occurs (e.g., invalid city name or API issue), an error message is returned.
    """
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    res = requests.get(url)
    data = res.json()

    if "error" in data:
        return f"Error: {data['error']['message']}"

    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']

    return f"In {city}, it's {temp}°C and {condition.lower()}."
