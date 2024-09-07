import csv
import datetime as dt
import pytz
import requests
import urllib
import uuid

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(country, unit):
    """open weather api"""
    api_key = '893cbbac726aa5674136bdefde03d5b5'

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={country}&units={unit}&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        not_found = "No City Found"
        return not_found
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']
        max_temp = weather_data.json()['main']['temp_min']
        min_temp = weather_data.json()['main']['temp_max']
        feels_like = = round(weather_data.json()['main']['feels_like'])
        humidity = = round(weather_data.json()['main']['humidity'])
        wind_speed = = round(weather_data.json()['wind']['speed'])
        
        humidity = = round(weather_data.json()['main']['humidity'])
        humidity = = round(weather_data.json()['main']['humidity'])

        return weather, temp
        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF")
        print(weather_data.json())
