import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

#load_dotenv loads the api_key from .env file
load_dotenv()
api_key = os.getenv('API_KEY') #os.getenv gets the value of the environment variable, in this case api_key

@dataclass #dataclass is used here to hold the data content we are getting from the weather_data    
class weather_data:
    main : str
    description : str
    icon : str
    temperature : int

def get_lat_lon(city_name, country_code,API_KEY):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_KEY}').json()
    try:
        data = resp[0]
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    except Exception:
        return None, None


def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    print(resp)
    data = weather_data(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperature = int(resp.get('main').get('temp'))
    )

    return data

def main(city_name, country_code):
    lat , lon = get_lat_lon (city_name, country_code, api_key )
    if lat is None or lon is None:
        return {"error": "The entered city or country is invalid"}
    else:
        weather_data = get_current_weather(lat,lon,api_key)
        return weather_data
    
