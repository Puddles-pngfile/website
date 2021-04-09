from flask import Flask, render_template, redirect
import random  





app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/diceroll")
def dice():
    return render_template("diceroll.html", dice=random.randint(1,6))

@app.route("/generator")
def generator():
    return render_template("number.html", num=random.randint(0,100))


@app.route("/snake")
def number():
    return render_template("snake.html")

@app.route("/gamestore")
def gamestore():
    return render_template("gamestore.html")








@app.route("/joke")
def joke():
    return render_template("joke.html")





if __name__ == "__main__":
    app.run()








    
































if __name__ == '__main__':
    app.run(debug=True)










