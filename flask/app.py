from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if requests.method == "POST":
        city = requests.form['city']
        country = requests.form['country']
        api_key = "###"

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity= weather_data['wind']['humidity']
        wind_speed = weather_data['wind']['speed']

        return render_template("result.html", temp=temp, humidity=humidity, win_speed=wind_speed, city=city)

    return render_template("index.html")
    # return '<h1>Hello!!</h1>'

#http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial