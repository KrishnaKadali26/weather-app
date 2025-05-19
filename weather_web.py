import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data.get("cod") != 200:
            return {"Error": data.get("message", "Invalid city")}
        return {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
        }
    except:
        return {"Error": "Request failed"}

st.title("🌦️ Weather Web App")
city = st.text_input("Enter City:")

if city:
    weather = get_weather(city)
    if "Error" in weather:
        st.error(weather["Error"])
    else:
        st.success("Weather Info:")
        for k, v in weather.items():
            st.write(f"**{k}**: {v}")
    