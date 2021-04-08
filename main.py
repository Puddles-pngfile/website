from flask import Flask, redirect, url_for, 
import random
app = Flask(__name__)


@app.route("/home")
def home():
    name = "web"
    return render_template("index.html")

    


@app.route('/RNGnumber')
def number():
    rand = random.randint(0,1000)
    
    

    rand = random.randint(0,100)
    return render_template("randnum.html")

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="PrivatePageAdminOnly"))



if __name__ == "__main__":
    app.run(debug=True)








