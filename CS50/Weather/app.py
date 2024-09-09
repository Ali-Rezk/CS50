from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup

app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)


# Configure CS50 Library to use SQLite database

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    lookedup = lookup("cairo","1","1")

    temp = lookedup[1]['temp_c']
    condition = lookedup[1]['condition']['text']
    wind_speed = lookedup[1]['wind_kph']
    wind_dir = lookedup[1]['wind_dir']
    pressure_mb = lookedup[1]['pressure_mb']
    humidity = lookedup[1]['humidity']
    feelslike_c = lookedup[1]['feelslike_c']
    vis_km = lookedup[1]['vis_km']
    icon = lookedup[1]['condition']['icon']
    current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, icon]
    print(current)
    print(lookedup[1])

    sunrise = lookedup[4]['sunrise']
    sunset = lookedup[4]['sunset']
    moonrise = lookedup[4]['moonrise']
    moonset = lookedup[4]['moonset']
    moon_phase = lookedup[4]['moon_phase']
    moon_illumination = lookedup[4]['moon_illumination']
    astra = [sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination]

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_time = now.split()

    return render_template("today.html", current=current, date_time=date_time, astra=astra)

@app.route("/hourly")
def hourly():
    return render_template("hourly.html")
