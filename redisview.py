from flask import Flask
from flask import render_template
from flask import request
import talk2redis

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template("home.html")

@app.route('/view', methods=['POST', 'GET'])
def keyview():
    if request.method == "POST":
        keystate = request.form
        job = keystate['rediskey']
        keyvalue = talk2redis.viewkey(job)
        #keyvalue = {"area1": "NONE", "area2": "RUNNING", "area3": "DONE"}
        return render_template("keyview.html", keydata = keyvalue, job = job)

    return render_template("home.html")

@app.route('/stopjob', methods = ['POST'])
def stopjob():
    job = request.form['rediskeyerror']
    talk2redis.set2error(job)
    keyvalue = talk2redis.viewkey(job)
    return render_template("keyview.html", keydata = keyvalue, job = job)
