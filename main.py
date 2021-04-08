from flask import Flask, redirect, url_for, render_template
import random
app = Flask(__name__)


@app.route("/home")
def home():
    name = "Verge"
    return render_template("index.html")


@app.route("/RNGnumber")
def number():
    rand = random.randint(0,100)
    return render_template("randnum.html", rand = rand )










