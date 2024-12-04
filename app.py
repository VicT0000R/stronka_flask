from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
# Własne funkcje
from functions import *
from db import * 



app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

# DB connection
db.init_app(app)
with app.app_context():
    try:
        db.create_all()
        print("Połączenie z bazą danych zostało nawiązane.")
    except Exception as e:
        print(f"Błąd połączenia z bazą danych: {e}")


@app.route("/", methods=["GET", "POST"])
def login():

    if session.get('authorization') == True:
        return render_template("base.html", session=session)

    if request.method == "GET":
        return render_template("login.html")
    

    elif request.method == "POST":
        req  = request.form.to_dict()
        user_valid, message = user_exists(req)
        if user_valid:
            session['authorization'] = True
            return render_template("base.html",session=session)
        else:
            return render_template("login.html", message=message)
        

        
@app.route("/register", methods=["GET", "POST"])
def register(): 
    if request.method == "GET":
        return render_template("register.html")
    
    elif request.method == "POST":
        req  = request.form.to_dict()
        user_valid, message = create_user(req)
        if user_valid:
            session['authorization'] = True
            return redirect(url_for('login'))
        else:
            return render_template("register.html", message=message)
        

@app.route("/logout")
def logut():
    session.clear()
    return redirect(url_for('login'))
    

if __name__ == '__main__':    
    app.run(debug=True)