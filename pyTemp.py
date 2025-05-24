import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()


def getTemperature():
    print("\n************ ☁️☁️☁️  Getting Temperature .... ☁️☁️☁️************")
    city = input("Enter the City Name 🌆  : \n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather = requests.get(request_url).json()
    print(f"Current Weather for {weather["name"]}")
    print(f"The temperature is {weather["main"]["temp"]}°C")


getTemperature()