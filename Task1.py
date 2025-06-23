import requests
import matplotlib.pyplot as plt
from datetime import datetime


city_name = 'bengaluru'
API_key = '167e8e2058edf7e603f46cffe20a5d2e'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()


    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print('In', city_name)
    print('Weather is:', weather_desc)
    print('Temperature is:', temp)
    print('Humidity is:', humidity)
    print('Pressure is:', pressure)

    
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [temp, humidity, pressure]

    ''' Bar Chart visualisation '''
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title(f'Current Weather in {city_name}({weather_desc.capitalize()})\n{now}')
    plt.ylabel('Values')
    plt.tight_layout()
    plt.show()

    '''line chart visualisation'''
    plt.figure(figsize=(8, 5))
    plt.plot(labels, values, marker='o', linestyle='-', color='orange')
    plt.title(f'Weather Line Chart - {city_name}({weather_desc.capitalize()})\n{now}')
    plt.ylabel('Values')
    plt.tight_layout()
    plt.show()

    '''pie chart visualisation'''
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightcoral', 'lightgoldenrodyellow'])
    plt.title(f'Weather Composition - {city_name}({weather_desc.capitalize()})\n{now}')
    plt.tight_layout()
    plt.show()
