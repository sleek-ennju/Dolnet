#!/usr/bin/env python3
"""Module that resolves all default APIs for Dolianet"""
from sqlalchemy.orm.exc import NoResultFound
from models.engine.users_db import Users
from api.v1.views import app_views
from datetime import datetime
from flask import Flask, jsonify, request, render_template, redirect, url_for


app = Flask(__name__)
us = Users()
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app_views.route('/', methods=["POST"], strict_slashes=False)
def homepage():
    """Renders the landing page of Dolianet"""
    return render_template("~/Dolnet/dolianet.com/index-2.html")

@app_views.route('/login', methods=["POST"], strict_slashes=False)
def hello_login():
    """Renders the login page"""
    return render_template("~/Dolnet/dolianet.com/login.html")

@app_views.route('/register', methods=["POST"], strict_slashes=False)
def hello_register():
    """Renders the register page"""
    return render_template("~/Dolnet/dolianet.com/register.html")

@app_views.route('/app.py', methods=["POST", "GET"], strict_slashes=False)
def login_validation():
    """Validates the login credentials"""
    if "login" in request.form:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            try:
                user_login = us.find_user_by(email=email, password=password)
                if user_login:
                    print(user_login.user_name)
                    return redirect(url_for("~/Dolnet/dolianet.com/dashboard/main-dashboard.html"))
                else:
                    print("Could not find login details")
                    return render_template("~/Dolnet/dolianet.com/index-2.html")
            except Exception as e:
                print(e)

def register_user():
    """Registers the user"""
    if "register" in request.form:
        if request.method == "POST":
            email = request.form["email"]
            user_name = request.form["uname"]
            password = request.form["password"]
            date_created = datetime.now()
            date_updated = datetime.now()
            try:
                reg_user = us.create_user(user_id, user_name, email, password,
                                          date_created, date_updated)
                if reg_user:
                    print(reg_user.email)
                    return redirect(url_for("~/Dolnet/dolianet.com/wallet.html"))
                else:
                    return jsonify({"Error": "Something went wrong"}), 401

            except Exception as err:
                print(err)
                return jsonify({"error": "Could not register the user"}), 500

def collect_phrase():
    """Registers the user phrase"""
    if "wallet" in request.form:
        if request.method == "PATCH":

