from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from helpers import apology, login_required, lookup
import geocoder
import time
from flask_cors import CORS
import pytz

app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///weather.db")

# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Log user in"""

#     # Forget any user_id
#     session.clear()

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":
#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username", 403)

#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password", 403)

#         # Query database for username
#         rows = db.execute(
#             "SELECT * FROM users WHERE username = ?", request.form.get("username")
#         )

#         # Ensure username exists and password is correct
#         if len(rows) != 1 or not check_password_hash(
#             rows[0]["hash"], request.form.get("password")
#         ):
#             return apology("invalid username and/or password", 403)

#         # Remember which user has logged in
#         session["user_id"] = rows[0]["id"]

#         # Redirect user to home page
#         return redirect("/")

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     """Register user"""
#     if request.method == "POST":
#         reg_username = request.form.get("username")
#         reg_password = request.form.get("password")
#         confirmation = request.form.get("confirmation")
#         if not reg_username:
#             return apology("must provide username", 400)
#         elif not reg_password:
#             return apology("must provide password", 400)
#         elif not confirmation:
#             return apology("must provide confirmation", 400)
#         elif confirmation != reg_password:
#             return apology("password and confirmation does not match", 400)
#         hash_password = generate_password_hash(reg_password, method='pbkdf2', salt_length=16)
#         try:
#             db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
#                        reg_username, hash_password)
#         except ValueError:
#             return apology("username is taken")
#         return render_template("login.html")

#     else:
#         return render_template("register.html")

@app.route("/",methods =["POST","GET"])
def index():
    print(request.method)
    print(session)
    session["coords"] = [None, None]
    session["city"] = None
    if request.method == "POST":
        name = request.form.get("search")
        data = request.get_json()
        session['coords'] = [data['latitude'], data['longitude']]
        print(session)
        session["city"] = name
        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']

        location = [city, region, country]

        temp = lookedup[1]['temp_c']
        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        feelslike_c = lookedup[1]['feelslike_c']
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        dewpoint = lookedup[1]['dewpoint_c']
        icon = lookedup[1]['condition']['icon']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon]

        max_temp = lookedup[2][0]['day']['maxtemp_c']
        avg_temp = lookedup[2][0]['day']['avgtemp_c']
        min_temp = lookedup[2][0]['day']['mintemp_c']
        rain_chance = lookedup[2][0]['day']['daily_chance_of_rain']
        snow_chance = lookedup[2][0]['day']['daily_chance_of_snow']
        condition = lookedup[2][0]['day']['condition']['text']
        icon = lookedup[2][0]['day']['condition']['icon']
        daily = [round(max_temp), round(avg_temp), round(min_temp), rain_chance, snow_chance, condition, icon]

        sunrise = lookedup[4]['sunrise']
        sunset = lookedup[4]['sunset']
        moonrise = lookedup[4]['moonrise']
        moonset = lookedup[4]['moonset']
        moon_phase = lookedup[4]['moon_phase']
        moon_illumination = lookedup[4]['moon_illumination']
        astro = [sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination]

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        date_time = now.split()

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)
    else:
        session["coords"] = [None, None]
        if isinstance(session['coords'][0], float):
            print("float")
        else:
            print("nothing")
        city = "-"
        region = "-"
        country = "-"

        location = [city, region, country]

        temp = "-"
        condition = "-"
        wind_speed = "-"
        wind_dir = "-"
        pressure_mb = "-"
        humidity = "-"
        feelslike_c = "-"
        vis_km = "-"
        uv = "-"
        dewpoint = "-"
        icon = "-"
        current = [temp, condition, feelslike_c, wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon]

        max_temp = "-"
        avg_temp = "-"
        min_temp = "-"
        rain_chance = "-"
        snow_chance = "-"
        condition = "-"
        icon = "-"
        daily = [max_temp, avg_temp, min_temp, rain_chance, snow_chance, condition, icon]

        sunrise = "-"
        sunset = "-"
        moonrise = "-"
        moonset = "-"
        moon_phase = "-"
        moon_illumination = "-"
        astro = [sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination]

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        date_time = now.split()
        return render_template("temp.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)


@app.route("/today",methods =["POST","GET"])
def today():

    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")

        if name:
            session["city"] = name
            print(name)
        elif session["coords"]:
            name = session["coords"]
        else:
            name = session["city"]

        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']

        location = [city, region, country]

        temp = lookedup[1]['temp_c']
        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        feelslike_c = lookedup[1]['feelslike_c']
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        dewpoint = lookedup[1]['dewpoint_c']
        icon = lookedup[1]['condition']['icon']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon]

        max_temp = lookedup[2][0]['day']['maxtemp_c']
        avg_temp = lookedup[2][0]['day']['avgtemp_c']
        min_temp = lookedup[2][0]['day']['mintemp_c']
        rain_chance = lookedup[2][0]['day']['daily_chance_of_rain']
        snow_chance = lookedup[2][0]['day']['daily_chance_of_snow']
        condition = lookedup[2][0]['day']['condition']['text']
        icon = lookedup[2][0]['day']['condition']['icon']
        daily = [round(max_temp), round(avg_temp), round(min_temp), rain_chance, snow_chance, condition, icon]

        sunrise = lookedup[4]['sunrise']
        sunset = lookedup[4]['sunset']
        moonrise = lookedup[4]['moonrise']
        moonset = lookedup[4]['moonset']
        moon_phase = lookedup[4]['moon_phase']
        moon_illumination = lookedup[4]['moon_illumination']
        astro = [sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination]

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        date_time = now.split()

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)

    else:
        print(session)
        if session["city"] is not None:
            name = session["city"]
        elif session["coords"] is not None:
            name = session["coords"]
        else:
            return redirect("temp.html")
        print(name)
        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']

        location = [city, region, country]

        temp = lookedup[1]['temp_c']
        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        feelslike_c = lookedup[1]['feelslike_c']
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        dewpoint = lookedup[1]['dewpoint_c']
        icon = lookedup[1]['condition']['icon']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon]

        max_temp = lookedup[2][0]['day']['maxtemp_c']
        avg_temp = lookedup[2][0]['day']['avgtemp_c']
        min_temp = lookedup[2][0]['day']['mintemp_c']
        rain_chance = lookedup[2][0]['day']['daily_chance_of_rain']
        snow_chance = lookedup[2][0]['day']['daily_chance_of_snow']
        condition = lookedup[2][0]['day']['condition']['text']
        icon = lookedup[2][0]['day']['condition']['icon']
        daily = [round(max_temp), round(avg_temp), round(min_temp), rain_chance, snow_chance, condition, icon]

        sunrise = lookedup[4]['sunrise']
        sunset = lookedup[4]['sunset']
        moonrise = lookedup[4]['moonrise']
        moonset = lookedup[4]['moonset']
        moon_phase = lookedup[4]['moon_phase']
        moon_illumination = lookedup[4]['moon_illumination']
        astro = [sunrise,sunset,moonrise,moonset,moon_phase,moon_illumination]

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        date_time = now.split()
        print(session["coords"])
        print(session["city"])

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)


@app.route("/hourly", methods = ["POST","GET"])
def hourly():
    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")

        session["city"] = name
        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]

        for i in range(0,5):
            ss = hourly[i]['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            hourly[i]['date'] = date.strftime("%A,%B %d")

            for x in range(0,24):
                n = hourly[i]['hour'][x]
                n['time'] = n['time'].split()[1]
                hourly[i]['hour'][x] = n


        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %H:%M %Z %z')
        date_time = now.split()
        ss = str(datetime.now(timezone)).split('+')
        date_time[3] = ss[1]


        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly)

    else:
        print(session)

        if session["city"] is not None:
            name = session["city"]
        elif session["coords"]:
            name = session["coords"]

        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]

        for i in range(0,5):
            ss = hourly[i]['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            hourly[i]['date'] = date.strftime("%A,%B %d")

            for x in range(0,24):
                n = hourly[i]['hour'][x]
                n['time'] = n['time'].split()[1]
                hourly[i]['hour'][x] = n


        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %H:%M %Z %z')
        date_time = now.split()
        ss = str(datetime.now(timezone)).split('+')
        date_time[3] = ss[1]


        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly)



@app.route("/daily", methods = ["POST", "GET"])
def daily():
    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")

        lookedup = lookup(name)
        session["city"] = name

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]

        for i in range(0,5):
            ss = hourly[i]['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            hourly[i]['date'] = date.strftime("%A,%B %d")
            hourly[i]['date_day'] = date.strftime("%A, %d")
            hourly[i]['day_day'] = date.strftime("%d")

            for x in range(0,24):
                n = hourly[i]['hour'][x]
                n['time'] = n['time'].split()[1]
                hourly[i]['hour'][x] = n


        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %H:%M %Z %z')
        date_time = now.split()
        ss = str(datetime.now(timezone)).split('+')
        date_time[3] = ss[1]


        return render_template("daily.html", location=location, date_time=date_time, hourly=hourly)

    else:
        print(session["coords"])

        if session["city"] is not None:
            name = session["city"]
        elif session["coords"]:
            name = session["coords"]

        lookedup = lookup(name)

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]

        for i in range(0,5):
            ss = hourly[i]['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            hourly[i]['date'] = date.strftime("%A,%B %d")
            hourly[i]['date_day'] = date.strftime("%A, %d")
            hourly[i]['day_day'] = date.strftime("%d")

            for x in range(0,24):
                n = hourly[i]['hour'][x]
                n['time'] = n['time'].split()[1]
                hourly[i]['hour'][x] = n


        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %H:%M %Z %z')
        date_time = now.split()
        ss = str(datetime.now(timezone)).split('+')
        date_time[3] = ss[1]


        return render_template("daily.html", location=location, date_time=date_time, hourly=hourly)


@app.route("/history")
def history():
    data = request.args
    print(data)

    return render_template("history.html")

