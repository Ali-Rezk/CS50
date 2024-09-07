import requests
import datetime as dt

api_key = '893cbbac726aa5674136bdefde03d5b5'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    sunrise = dt.datetime.utcfromtimestamp(int(weather_data.json()['sys']['sunrise']) + int(['timezone']))

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
    print(weather_data.json())
    print(sunrise)

