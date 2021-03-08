from flask import Flask, request, render_template
import datetime
import json
import threading
import requests
import time
import random
from bs4 import BeautifulSoup

# http://localhost:5000/?num=1234 to sent sensor data
# http://localhost:5000/display to display all the sensor data
# http://localhost:5000/weather to display the weather message

all_num = []
string = "Heart Rate: {:.2f} bpm / SpO2: {:.2f} %"

app = Flask(__name__)


def scrap():
    html = requests.get('https://news.pchome.com.tw/weather/').content
    soup = BeautifulSoup(html, 'html.parser')
    humidity = soup.select(
        '#container > div.bx-wrapper > section:nth-child(4) > div > div.dt-table > p:nth-child(2) > span'
    )[0].text
    temp = soup.select(
        '#container > div.bx-wrapper > section.today_cont > div.right_today > div.temp > div:nth-child(1) > span.num'
    )[0].text
    weather = soup.select(
        '#wptab > div.pcb.active > ul > li:nth-child(1) > p.wea'
    )[0].text
    return weather, temp, humidity


weather, temp, humidity = scrap()


@app.route("/", methods=['GET'])
def index():
    global all_num, weather
    heart_rate = random.uniform(69, 74)
    sp = random.uniform(94, 99)
    num = string.format(heart_rate, sp)

    now = datetime.datetime.now()
    data = {"now": now, "data": num}
    all_num += [{
        "now": now.strftime('%a, %d %b %Y %H:%M:%S'),
        "data": num,
    }]
    return data


@app.route("/weather", methods=['GET'])
def view():
    global weather, temp, humidity
    now = datetime.datetime.now()
    if now.hour == 00:
        weather, temp, humidity = scrap()

    data = {
        "now": now.strftime('%a, %d %b %Y %H:%M:%S'),
        "weather": f"台北市: {weather}",
        "temperature": f"{temp}˚",
        "humidity": f"{humidity}"
    }
    return render_template(
        "index.html",
        all=json.dumps(data, indent=4, separators=(
            ',', ': '), ensure_ascii=False)
    )


@app.route("/display", methods=['GET'])
def display():
    global all_num
    return render_template(
        "index.html",
        all=json.dumps(all_num, indent=4, separators=(
            ',', ': '), ensure_ascii=False)
    )


def job():
    while 1:
        time.sleep(5)
        requests.get("http://127.0.0.1:5000/")
        requests.get("http://127.0.0.1:5000/weather")


# @app.route("/", methods=['GET'])
# def index():
#     global all_num
#     num = request.args.get('num')
#     if num == None:
#         return {"error": "no num parameter"}
#     now = datetime.datetime.now()
#     data = {"now": now, "num": num}
#     all_num += [{"now": now.strftime('%a, %d %b %Y %H:%M:%S'), "num": num}]
#     return data

# @app.route("/display", methods=['GET'])
# def view():
#     global all_num
#     return {"all_data": all_num}
if __name__ == '__main__':
    t = threading.Thread(target=job)
    t.start()
    app.debug = True
    app.run()
