#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__, template_folder='../')
app.config['SQLALCHEMY_DATABASE_URI'] =\
        "mysql://dolianet_dev:senjuu@localhost:3306/dolianet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
        return render_template("wallet.html")

    @app.route('/dashboard.html', strict_slashes=False)
    def hello_dashboard():
        """Renders the dashboard page"""
        return render_template("dashbaord/main-dashboard.html")

    # Defining APIs
    @app.route('/app.py', methods=["POST", "GET", "PATCH"], strict_slashes=False)
    def registration():
        """Handles the login, register and collect phrase functionalities"""
        if "login" in request.form:
            if request.method == "POST":
                email = request.form['email']
                password = request.form['password']
                try:
                    user = User.query.filter_by(email=email, password=password).all()
                    if user:
                        print(user)
                        return redirect(url_for("hello_dashboard"))
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
                        db.session.add(register_user)
                        db.session.commit()
                        print(register_user.user_name)
                        return redirect(url_for("wallet"))
                    else:
                        db.session.rollback()
                        print("Error: Could not register user account")
                        return redirect(url_for("register"))
                except Exception as err:
                    print(err)
