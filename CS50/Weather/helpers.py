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


def lookup(country, days, hour):

    api_key = '5aba5ac55b984050bfa230233240709'

    currentWeather_data = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={country}&aqi=no"
    )

    daily_data = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={country}&days={days}&aqi=yes&alerts=no"
    )

    hourly_data = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={country}&days={days}&aqi=yes&alerts=no&hour={hour}"
    )

    try:
        # date, max/avg/min temp, avg wind speed, avg humidity, rain chance, snow chance, condition, icon
        daily = daily_data.json()['forecast']['forecastday']
        # time, temp, is_day?, condition, wind speed/dir, humidity, feelslike, vis, uv?, gust?, snow_cm?, icon, cloud cover, pressure
        hourly = hourly_data.json()['forecast']['forecastday'][0]['hour']
        # sunrise, sunset, moon_phase, moon_illumination, moonset, moonrise
        astro = hourly_data.json()['forecast']['forecastday'][0]['astro']
        # name, region, country, localtime
        location = currentWeather_data.json()['location']
        # temp, is_day?, condition, wind speed/dir, humidity, feelslike, vis, uv?, gust?, snow_cm?, icon, dewpoint
        current = currentWeather_data.json()['current']

        return location, current, daily, hourly, astro

    except:
        not_found = "No City Found"
        return not_found

