import requests
import os

API_KEY = '0be2b07e4c8615ce85a82c8551063bc8'  # Replace with your OpenWeatherMap API Key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()
