from flask import Flask, redirect, url_for
import random
app = Flask(__name__)


@app.route('/')
def home():
    name = "Verge"
    return render_template("index.html")

@app.route("/numgen"):
def numgen():
    rand = random.randint(0,1000)
    return render_template("randnum.html")
    






