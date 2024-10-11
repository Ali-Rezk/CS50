from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from datetime import datetime, timedelta
from helpers import apology, lookup
import re
import pytz

app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def initialize_session():
    if 'coords' not in session:
        session['coords'] = [None, None]
    if 'city' not in session:
        session['city'] = None
    if 'unit' not in session:
        session['unit'] = None

@app.route("/",methods =["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form.get("search")
        symbol = request.form.get("symbol")
        change_unit = True
        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
            change_unit = False
        except:
            print("error")
        if name:
            session["city"] = name
        elif session["coords"]:
            name = session["coords"]
        else:
            name = session["city"]
        
        lookedup = lookup(name)

        if lookedup == "No City Found":
            location_missing = True
            return apology("today.html", location_missing ,"City not found")
        
        city = lookedup[0]['name']
        region = lookedup[0]['region']
        country = lookedup[0]['country']

        location = [city, region, country]

        if change_unit:
            if symbol == "F°":
                temp = lookedup[1]['temp_f']
                feelslike_c = lookedup[1]['feelslike_f']
                dewpoint = lookedup[1]['dewpoint_f']
                max_temp = lookedup[2][0]['day']['maxtemp_f']
                avg_temp = lookedup[2][0]['day']['avgtemp_f']
                min_temp = lookedup[2][0]['day']['mintemp_f']
                session["unit"] = "F°"
                unit1 = "F°"
                unit2 = "C°"
            else:
                temp = lookedup[1]['temp_c']
                feelslike_c = lookedup[1]['feelslike_c']
                dewpoint = lookedup[1]['dewpoint_c']
                max_temp = lookedup[2][0]['day']['maxtemp_c']
                avg_temp = lookedup[2][0]['day']['avgtemp_c']
                min_temp = lookedup[2][0]['day']['mintemp_c']
                session["unit"] = "C°"
                unit1 = "C°"
                unit2 = "F°"

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
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, round(dewpoint), icon, is_day]

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
        session["unit"] = None
        city = "-"
        region = "-"
        country = "-"

        location = [city, region, country]

        if session["unit"] == "F°":
            unit1 = "F°"
            unit2 = "C°"
        else:
            unit1 = "C°"
            unit2 = "F°"

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
        return render_template("temp.html",location=location, current=current, date_time=date_time, astro=astro, 
                                    daily=daily, unit1=unit1, unit2=unit2)


@app.route("/today",methods =["POST","GET"])
def today():
    if request.method == "POST":
        name = request.form.get("search")
        symbol = request.form.get("symbol")
        change_unit = True
        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
            change_unit = False
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
        
        if change_unit:
            if symbol == "F°":
                temp = lookedup[1]['temp_f']
                feelslike_c = lookedup[1]['feelslike_f']
                dewpoint = lookedup[1]['dewpoint_f']
                max_temp = lookedup[2][0]['day']['maxtemp_f']
                avg_temp = lookedup[2][0]['day']['avgtemp_f']
                min_temp = lookedup[2][0]['day']['mintemp_f']
                session["unit"] = "F°"
                unit1 = "F°"
                unit2 = "C°"
            else:
                temp = lookedup[1]['temp_c']
                feelslike_c = lookedup[1]['feelslike_c']
                dewpoint = lookedup[1]['dewpoint_c']
                max_temp = lookedup[2][0]['day']['maxtemp_c']
                avg_temp = lookedup[2][0]['day']['avgtemp_c']
                min_temp = lookedup[2][0]['day']['mintemp_c']
                session["unit"] = "C°"
                unit1 = "C°"
                unit2 = "F°"

        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        
        icon = lookedup[1]['condition']['icon']
        is_day = lookedup[1]['is_day']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, round(dewpoint), icon, is_day]

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
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)
        
        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro, 
                                    daily=daily, unit1=unit1, unit2=unit2)
        
    else:
        if session["city"] is not None:
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

        if session["unit"] == "F°":
            temp = lookedup[1]['temp_f']
            feelslike_c = lookedup[1]['feelslike_f']
            dewpoint = lookedup[1]['dewpoint_f']
            max_temp = lookedup[2][0]['day']['maxtemp_f']
            avg_temp = lookedup[2][0]['day']['avgtemp_f']
            min_temp = lookedup[2][0]['day']['mintemp_f']
            unit1 = "F°"
            unit2 = "C°"
        else:
            temp = lookedup[1]['temp_c']
            feelslike_c = lookedup[1]['feelslike_c']
            dewpoint = lookedup[1]['dewpoint_c']
            max_temp = lookedup[2][0]['day']['maxtemp_c']
            avg_temp = lookedup[2][0]['day']['avgtemp_c']
            min_temp = lookedup[2][0]['day']['mintemp_c']
            session["unit"] == "C°"
            unit1 = "C°"
            unit2 = "F°"

        condition = lookedup[1]['condition']['text']
        wind_speed = lookedup[1]['wind_kph']
        wind_dir = lookedup[1]['wind_dir']
        pressure_mb = lookedup[1]['pressure_mb']
        humidity = lookedup[1]['humidity']
        vis_km = lookedup[1]['vis_km']
        uv = lookedup[1]['uv']
        icon = lookedup[1]['condition']['icon']
        is_day = lookedup[1]['is_day']
        current = [round(temp), condition, round(feelslike_c), wind_speed, wind_dir, pressure_mb, humidity, vis_km, uv, round(dewpoint), icon, is_day]

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
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("today.html",location=location, current=current, date_time=date_time, astro=astro,
                                     daily=daily, unit1=unit1, unit2=unit2)


@app.route("/hourly", methods = ["POST","GET"])
def hourly():
    if request.method == "POST":
        name = request.form.get("search")
        symbol = request.form.get("symbol")
        change_unit = True
        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
            change_unit = False
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

        if change_unit:
            if symbol == "F°":
                session["unit"] = "F°"
                unit1 = "F°"
                unit2 = "C°"
                unit = "f"
            else:
                session["unit"] = "C°"
                unit1 = "C°"
                unit2 = "F°"
                unit = "c"

        for day in hourly:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")
            
            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)
        

        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly, unit=unit ,unit1=unit1, unit2=unit2)
    
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
        
        if session["unit"] == "F°":
            unit1 = "F°"
            unit2 = "C°"
            unit = "f"
        else:
            unit1 = "C°"
            unit2 = "F°"
            unit = "c"

        hourly = lookedup[2]
        for day in hourly:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")
            
            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("hourly.html", location=location, date_time=date_time, hourly=hourly, unit=unit ,unit1=unit1, unit2=unit2)


@app.route("/daily", methods = ["POST", "GET"])
def daily():
    if request.method == "POST":
        name = request.form.get("search")
        symbol = request.form.get("symbol")

        change_unit = True
        try:
            data = request.get_json()
            session['coords'] = [data['latitude'], data['longitude']]
            change_unit = False
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
        
        if change_unit:
            if symbol == "F°":
                session["unit"] = "F°"
                unit1 = "F°"
                unit2 = "C°"
                unit = "f"
            else:
                session["unit"] = "C°"
                unit1 = "C°"
                unit2 = "F°"
                unit = "c"

        daily = lookedup[2]

        for day in daily:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")
            day['date_day'] = date.strftime("%A, %d")
            day['day_day'] = date.strftime("%d")
            
            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)


        return render_template("daily.html", location=location, date_time=date_time, daily=daily, unit=unit ,unit1=unit1, unit2=unit2)
    
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

        if session["unit"] == "F°":
            unit1 = "F°"
            unit2 = "C°"
            unit = "f"
        else:
            unit1 = "C°"
            unit2 = "F°"
            unit = "c"

        daily = lookedup[2]

        for day in daily:
            ss = day['date'].split("-")
            date = datetime(int(ss[0]), int(ss[1]), int(ss[2]))
            day['date'] = date.strftime("%A,%B %d")
            day['date_day'] = date.strftime("%A, %d")
            day['day_day'] = date.strftime("%d")
            
            for x in range(0,24):
                n = day['hour'][x]
                n['time'] = n['time'].split()[1]
                day['hour'][x] = n
        
        # used the help of bing chat for this part
        timezone = pytz.timezone(tz_id)
        now = datetime.now(timezone).strftime('%Y-%m-%d %I:%M %p %Z %z')
        date_time = now.split()
        match = re.search(r'([+-]\d{2}:\d{2})$', str(datetime.now(timezone)))
        date_time[4] = match.group(1)

        return render_template("daily.html", location=location, date_time=date_time, daily=daily, unit=unit ,unit1=unit1, unit2=unit2)