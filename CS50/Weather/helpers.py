import csv
import datetime as dt
import pytz
import requests
import urllib
import uuid
import pycountry

from flask import redirect, render_template, request, session
from functools import wraps


def apology(page, location_missing ,message, code=400):
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

    return render_template(page, location_missing = location_missing, top=code, bottom=escape(message)), code

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


def lookup(country):
    api_key = '5aba5ac55b984050bfa230233240709'
    days = 5

    try:
        lat = float(country[0])
        long = float(country[1])
        currentWeather_data = requests.get(
            f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{long}&aqi=no"
        )

        daily_data = requests.get(
            f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={lat},{long}&days={days}&aqi=yes&alerts=no"
        )

        currentWeather_data.raise_for_status()

    except:
        currentWeather_data = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={country}&aqi=no"
        )

        daily_data = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={country}&days={days}&aqi=yes&alerts=no"
        )




    # hourly_data = requests.get(
    #     f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={country}&days={days}&aqi=yes&alerts=no&hour={hour}"
    # )

    # history = requests.get(
    #     f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={country}&dt={date}"
    # )

    try:
        # date, max/avg/min temp, avg wind speed, avg humidity, rain chance, snow chance, condition, icon
        daily = daily_data.json()['forecast']['forecastday']
        # time, temp, is_day?, condition, wind speed/dir, humidity, feelslike, vis, uv?, gust?, snow_cm?, icon, cloud cover, pressure, dew_point
        hourly = daily_data.json()['forecast']['forecastday'][0]['hour']
        # sunrise, sunset, moon_phase, moon_illumination, moonset, moonrise
        astro = daily_data.json()['forecast']['forecastday'][0]['astro']
        # name, region, country, localtime
        location = currentWeather_data.json()['location']
        # temp, is_day?, condition, wind speed/dir, humidity, feelslike, vis, uv?, gust?, snow_cm?, icon, dewpoint
        current = currentWeather_data.json()['current']

        return location, current, daily, hourly, astro

    except:
        not_found = "No City Found"
        return not_found

def search(city):
    api = "893cbbac726aa5674136bdefde03d5b5"

    all_data = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}"
    )

    print(all_data.json())
    # Example usage
    # country_name = "united kingdom"
    # country_code = country_name_to_code(country_name)
    # print(f"The country code for {country_name} is {country_code}")
    for row in all_data:
        data = [row['name'], row['country'], row['state']]
    return data


def country_name_to_code(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        return country.alpha_2  # or country.alpha_3 for three-letter codes
    except LookupError:
        return None

    