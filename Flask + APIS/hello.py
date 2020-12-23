from flask import Flask, render_template
from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'

darksky = DarkSky(API_KEY)

latitude = 18.3006576
longitude = -98.6068401
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print("Temperature")
print(forecast.currently.temperature)

print("Time Zone")
print(forecast.timezone)

forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
forecast.alerts # [Alert]. Can be finded at darksky/forecast.py
app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"	
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "About"	
    return render_template("about.html",title=title)

@app.route("/contact")
def contact():
    title = "Contact"	
    return render_template("contact.html",title=title)
