import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            return {"Error": data.get("message", "Invalid city name.")}

        return {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Feels Like": f"{data['main']['feels_like']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
    except:
        return {"Error": "Failed to get weather"}

def show_weather():
    city = entry.get()
    result = get_weather(city)
    if "Error" in result:
        messagebox.showerror("Error", result["Error"])
    else:
        info = "\n".join([f"{k}: {v}" for k, v in result.items()])
        output.config(text=info)

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn = tk.Button(root, text="Get Weather", command=show_weather)
btn.pack()

output = tk.Label(root, text="", justify="left")
output.pack(pady=10)

root.mainloop()
