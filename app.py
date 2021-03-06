from flask import Flask, request
import datetime
import json

# http://localhost:5000/?num=1234 to sent senser data
# http://localhost:5000/display to get all the data

all_num = []
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    global all_num
    num = request.args.get('num')
    if num == None:
        return {"error": "no num parameter"}
    now = datetime.datetime.now()
    data = {"now": now, "num": num}
    all_num += [{"now": now.strftime('%a, %d %b %Y %H:%M:%S'), "num": num}]
    return data


@app.route("/display", methods=['GET'])
def view():
    global all_num
    return {"all_data": all_num}


if __name__ == '__main__':
    app.run()
