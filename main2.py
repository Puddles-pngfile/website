from flask import Flask, render_template
import random  





app = Flask(__name__)

@app.route("/diceroll")
def dice():
    return render_template("diceroll.html", dice=random.randint(1,6)



@app.route("/generator")
def number():
    return render_template("number.html", num=random.randint(0,100)



@app.route("/diceroll")
def dice():
    return render_template("diceroll.html", num2=random.randint(1,6))



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/joke")
def joke():
    return render_template("joke.html")

    
































if __name__ == '__main__':
    app.run(debug=True)










