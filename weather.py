import json
from logging import root
from tkinter import *
import tkinter as tk
import requests
import time

# root = Tk()

def getWeather(canvas):
    city = textfield.get()
    api = 'https://api.openweathermap.org/data/2.5/weather?q=' + str(city) + '&appid=91026a32e20292e7883094431a6b1d5a'
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    feels = int(json_data['main']['"feels_like"'] - 273.15)
    max_temp = int(json_data['main']['temp_min'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    sunrise = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunset'] - 21600))

    final_info = condition + '\n' + str(temp) + '°C'
    final_data = '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min Temp: ' + str(
        min_temp) + '\n' + 'Sunrise: ' + str(sunrise) + '\n' + 'Sunset: ' + str(sunset)

    label1.config(text=final_info)
    label2.config(text=final_data)

    # print(final_info)
    # print(final_data)

    # print(city)

canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title('Weather App')

f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

textfield = Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
