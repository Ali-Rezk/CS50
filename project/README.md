# Sunny
#### Video Demo:  <[Sunny project](https://youtu.be/tsq8UKf9C7k)>
#### Description:
Sunny is a weather web application.
which was created using html, css, javascript and some elemnets from bootstrap in the frontend.
as for the backend it was made using python and flask as the web framework.
the project uses a weather api called [weather api](https://www.weatherapi.com/) which provides all the weather data used in this project.

## python
### app.py
let us start with the backend specifically app.py where most of the code is written.
it starts with configuring the session settings then assigning session with keys and values before everything starts.

app.py handles the user's provided data (user's location, searched location) then uses the lookup function provided from the helpers.py which handles the api requests then returns back the data of that location and then it is handled by app.py and then sent to the suitable html to be shown to the user.
the data sent to the html changes depending on the unit that the user chose.

also app.py handles any error that may happen.

### helpers.py
#### lookup
lookup function handles all api requests which uses the user's location provided by app.py then returns the data back to app.py.

lookup takes two types of arguments it takes the city name (string) or the coords of the user's city (float) then tries to request the data from the api with exception handling in case of an error then returns either the data of the city or "No City Found" which is then handled in app.py 

#### apology
apology function renders apology massage in case of an error and takes four arguments.

* **page:** the html page that is needed to be rendered
* **location_missing:** a boolean variable 
* **message:** the apology massage
* **code:** the error code which is 400 by default

## html
### Note
the website is compatable with every screen size, i.e., smart phones, tablets, laptop or desktop.

### layout
this is the layout of the website which contains the global container, the logo, search bar, nav bar, the footer and the script for changing units.

### temp
then we go to the index (homepage) which is the defualt page for when the user opens the site it appears with no data because it was not yet given any data from the user like current location or a specific location to look up so the first thing the user is asked to allow the access to their current location if they allow the access then they can simply choose one of the three pages to go to (today, hourly, daily) then all the data of thier current location's weather will be shown.
or they can block the access to thier current location and just use the search bar to look up a specific city then they will be redirected to the today route and see all the weather data.

### Note
the following htmls allow the user to change the temperature unit from celsius to fahrenheit or vise versa.

if the user didn't provide any location then "location_missing" will be TRUE so the apology page will appear instead of the weather details but if the user provided a location then "location_missing" will be FALSE so the weather details will appear instead.

the location shown on google maps is the same location the user provided.

As for the script all it does is to get the user's coords and then sends it to python.

### today
this page contains the current weather of the user's provided location.

the background image for the current weather changes depending on if it is day or night, the moons image also changes depending on the moon phase.

in case it is a smart phone screen the layout of some elements will change for example:

* **table_s** is for small screens it will be displayed in case of the website being viewed in a smaller device and it will show two smaller tables instead of a single big one and if the device is not small then it will not be displayed and "table_l" will be displayed instead which is a single big table instead of two.

* **stats_s** is also for smaller devices and it contains a single big table with two columns, if the device is not small then "stats" will be displayed instead with two tables with "vl" as a separation between them

### hourly
this page contains the hourly weather forecast of 3 days for the user's provided location.

the first section shows the name of the city, region and country. 
the second sections shows date, time and timezone.

then two loops are implemented to go through every hour in each day to show the required data.

in case it is a smart phone screen the layout of some elements will change for example:

**hourly-body_s :** is for small screens it will be displayed in case of the website being viewed in a smaller device and it will show three tables instead of two with the third table being the data that was in the accordion button.
if not in a small screen "hourly-body" will be displayed instead with two tables and the data of the third table will be displayed in the accordion button.

### daily
this page contains the daily weather forecast of 3 days for the user's provided location.

the first section shows the name of the city, region and country. 
the second sections shows date, time and timezone.

then a loop is implemented to go through each day to show the required data.

in case it is a smart phone screen the layout of some elements will change for example:

**daily-body_s :** is for small screens it will be displayed in case of the website being viewed in a smaller device and it will show four tables instead of three with the fourth table being the data that was in the accordion button.
if not in a small screen "hourly-body" will be displayed instead with three tables and the data of the fourth table will be displayed in the accordion button.