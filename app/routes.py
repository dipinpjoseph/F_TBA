from app import app
from flask import render_template
import os
from flask import Response

@app.route('/')
def index():    
    data = {}
    data["title"] = "The Beginner's Arsenal"
    data["desc"] = "Home Page of The Beginner's Arsenal"

    return render_template('index.html', data=data)

@app.route('/ads.txt')
def ads_google():
    with open("app/ads.txt", "r") as f:
        con = f.read()
    return(Response(con, mimetype='text/plain'))

@app.route('/QR-Code-Generator')
def qr_code_gen():
    print(os.getcwd())
    return render_template("QR-Code-Generator.html")

@app.route('/Bar-Code-Generator')
def bar_code_gen():
    return render_template("Bar-Code-Generator.html")
