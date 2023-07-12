import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    city = city_entry.get()
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API")}&q={city}&lang={"pt_br"}&units=metric'
    weather_data = requests.get(request_url).json()
    result_label['text'] = f'{weather_data["name"]}\n' \
                           f'Temperatura de: {weather_data["main"]["temp"]} Celsius\n' \
                           f'Sensação Termica: {weather_data["main"]["feels_like"]} Celsius e com {weather_data["weather"][0]["description"]}.'

root = tk.Tk()
root.title('Consulta o Clima Agora')

city_label = tk.Label(root, text='Por favor coloque o nome da Cidade')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text='Consultar', command=get_current_weather)
submit_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
