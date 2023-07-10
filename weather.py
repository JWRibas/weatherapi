import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n***Consulta o Clima Agora***\n')

    city = input('\nPor favor coloque o nome da Cidade\n')


    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API")}&q={city}&units=metric'

    
    
    #print(request_url)

    weather_data = requests.get(request_url).json()

    #pprint(weather_data)
    print(f'\nClima hoje para: {weather_data["name"]}')
    print(f'\nA Temperatura é: {weather_data["main"]["temp"]}')
    print(f'\nA Sensação Termica é de: {weather_data["main"]["fells_like"]} and {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
    get_current_weather()