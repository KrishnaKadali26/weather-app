import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Feels Like": f"{data['main']['feels_like']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return {"Error": "City not found or API key issue."}

def display_weather(weather_data):
    print("\n🌦️ Weather Info:")
    for key, value in weather_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    weather_info = get_weather(city, api_key)
    display_weather(weather_info)
