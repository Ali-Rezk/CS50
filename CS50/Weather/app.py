from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from helpers import apology, login_required, lookup
import re
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


@app.route("/",methods =["POST","GET"])
def index():
    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")
        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
        except:
            print("error")
        print(session)
        if name:
            session["city"] = name
            print(name)
        elif session["coords"]:
            name = session["coords"]
        else:
            name = session["city"]

        print(name)
        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

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
        is_day = lookedup[1]['is_day']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon, is_day]

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

        return redirect("today")
    else:
        session["coords"] = [None, None]
        session["city"] = None
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
        symbol = request.form.get("symbol")
        print(symbol)
        # session['data'] = search(name)
        try:
            data = request.get_json()
            print(data)
            session['coords'] = [data['latitude'], data['longitude']]
        except:
            print("error")

        if name:
            session["city"] = name
        elif session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("today.html", location_missing ,"Please allow location access or use the search bar")
        print(name)

        lookedup = lookup(name)
        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]

        if symbol == "F°":
            temp = lookedup[1]['temp_f']
            feelslike_c = lookedup[1]['feelslike_f']
            dewpoint = lookedup[1]['dewpoint_f']
            max_temp = lookedup[2][0]['day']['maxtemp_f']
            avg_temp = lookedup[2][0]['day']['avgtemp_f']
            min_temp = lookedup[2][0]['day']['mintemp_f']
        else:
            temp = lookedup[1]['temp_c']
            feelslike_c = lookedup[1]['feelslike_c']
            dewpoint = lookedup[1]['dewpoint_c']
            max_temp = lookedup[2][0]['day']['maxtemp_c']
            avg_temp = lookedup[2][0]['day']['avgtemp_c']
            min_temp = lookedup[2][0]['day']['mintemp_c']

        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']

        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']

        icon = lookedup[1]['condition']['icon']
        is_day = lookedup[1]['is_day']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon, is_day]

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

        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)

    else:
        symbol = request.form.get("symbol")
        print(symbol)
        if session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("today.html", location_missing ,"Please allow location access or use the search bar")
        print(name)
        print("TEST")
        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]

        if symbol == "F°":
            temp = lookedup[1]['temp_f']
            feelslike_c = lookedup[1]['feelslike_f']
            dewpoint = lookedup[1]['dewpoint_f']
            max_temp = lookedup[2][0]['day']['maxtemp_f']
            avg_temp = lookedup[2][0]['day']['avgtemp_f']
            min_temp = lookedup[2][0]['day']['mintemp_f']
        else:
            temp = lookedup[1]['temp_c']
            feelslike_c = lookedup[1]['feelslike_c']
            dewpoint = lookedup[1]['dewpoint_c']
            max_temp = lookedup[2][0]['day']['maxtemp_c']
            avg_temp = lookedup[2][0]['day']['avgtemp_c']
            min_temp = lookedup[2][0]['day']['mintemp_c']

        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        icon = lookedup[1]['condition']['icon']
        is_day = lookedup[1]['is_day']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, dewpoint, icon, is_day]

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

        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, daily=daily)


@app.route("/hourly", methods = ["POST","GET"])
def hourly():
    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")

        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
        except:
            print("error")

        if name:
            session["city"] = name
        elif session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("today.html", location_missing ,"Please allow location access or use the search bar")
        print(session)
        print(session)
        lookedup = lookup(name)
        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

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
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)


        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly)

    else:
        if session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("hourly.html", location_missing ,"Please allow location access or use the search bar")

        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]
        for day in hourly:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")

            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n


        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly)


@app.route("/daily", methods = ["POST", "GET"])
def daily():
    print(request.method)
    print(session)
    if request.method == "POST":
        name = request.form.get("search")

        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
        except:
            print("error")

        if name:
            session["city"] = name
        elif session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("today.html", location_missing ,"Please allow location access or use the search bar")

        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

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
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)


        return render_template("daily.html", location=location, date_time=date_time, hourly=hourly)

    else:
        if session["city"] is not None:
            name = session["city"]
        elif session["coords"][0] is not None:
            name = session["coords"]
        else:
            location_missing = True
            return apology("daily.html", location_missing ,"Please allow location access or use the search bar")

        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")

        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']
        tz_id = lookedup[0]['tz_id']
        location = [city, region, country]


        hourly = lookedup[2]

        for day in hourly:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")
            day['date_day'] = date.strftime("%A, %d")
            day['day_day'] = date.strftime("%d")

            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n

        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("daily.html", location=location, date_time=date_time, hourly=hourly)


@app.route("/history")
def history():
    data = request.args
    print(data)

    return render_template("history.html")

@app.route("/radar")
def radar():
    return render_template("radar.html")

# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('q')
#     results = [item for item in session['data'] if query.lower() in item['name'].lower()]
#     return jsonify(results)
