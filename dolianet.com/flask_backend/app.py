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

    @app.route('/explore', strict_slashes=False)
    def explore():
        """Renders the explore page"""
        return render_template("explore.html")

    @app.route('/transactions', strict_slashes=False)
    def hello_transaction():
        """Renders the transaction page"""
        user_name = request.args.get('user_name')
        return render_template("transactions.html", user_name=user_name)

    @app.route('/transfer', strict_slashes=False)
    def hello_transfer():
        """Renders the transfer page"""
        user_name = request.args.get('user_name')
        return render_template("transfer.html", user_name=user_name)

    @app.route('/create', strict_slashes=False)
    def create_nft():
        """Renders the create_nft page"""
        return render_template("create_nft.html")

    @app.route('/create-collection', strict_slashes=False)
    def create_dashboard():
        """Renders the create_dashboard page"""
        return render_template("create_dashboard.html")

    @app.route('/withdraw', strict_slashes=False)
    def withdraw():
        """Renders the wthdraw page"""
        user_name = request.args.get('user_name')
        return render_template("withdraw.html", user_name=user_name)

    @app.route('/index', strict_slashes=False)
    def hello_index():
        return render_template('index.html')

    @app.route('/user-collection0b4e.html', strict_slashes=False)
    def user_profile01():
        return render_template("user-collection0b4e.html")

    @app.route('/user-collection1cc9.html', strict_slashes=False)
    def user_profile02():
        return render_template('user-collection1cc9.html')

    @app.route('/user-collection2baa.html', strict_slashes=False)
    def user_profile03():
        return render_template('user-collection2baa.html')

    @app.route('/user-collection2e6a.html', strict_slashes=False)
    def user_profile04():
        return render_template('user-collection2e6a.html')

    @app.route('/user-collection5aaa.html', strict_slashes=False)
    def user_profile05():
        return render_template('user-collection5aaa.html')

    @app.route('/user-collection5c72.html', strict_slashes=False)
    def user_profile06():
        return render_template('user-collection5c7a.html')

    @app.route('/user-collection5d72.html', strict_slashes=False)
    def user_profile07():
        return render_template('user-collection5d72.html')

    @app.route('/user-collection5fcc.html', strict_slashes=False)
    def user_profile08():
        return render_template('user-collection5fcc.html')

    @app.route('/user-collection7e1e.html', strict_slashes=False)
    def user_profile09():
        return render_template('user-collection7e1e.html')

    @app.route('/user-collection9de5.html', strict_slashes=False)
    def user_profile10():
        return render_template('user-collection9de5.html')

    @app.route('/user-collection12bb.html', strict_slashes=False)
    def user_profile11():
        return render_template('user-collection12bb.html')

    @app.route('/user-collection021c.html', strict_slashes=False)
    def user_profile12():
        return render_template('user-collection021c.html')

    @app.route('/user-collection57a9.html', strict_slashes=False)
    def user_profile13():
        return render_template('user-collection57a9.html')

    @app.route('/user-collection69ff.html', strict_slashes=False)
    def user_profile14():
        return render_template('user-collection69ff.html')

    @app.route('/user-collection423c.html', strict_slashes=False)
    def user_profile15():
        return render_template('user-collection423c.html')

    @app.route('/user-collection914b.html', strict_slashes=False)
    def user_profile16():
        return render_template('user-collection914b.html')

    @app.route('/user-collection4824.html', strict_slashes=False)
    def user_profile17():
        return render_template('user-collection4824.html')

    @app.route('/user-collection6010.html', strict_slashes=False)
    def user_profile18():
        return render_template('user-collection6010.html')

    @app.route('/user-collection8106.html', strict_slashes=False)
    def user_profile19():
        return render_template('user-collection8106.html')

    @app.route('/user-collection8756.html', strict_slashes=False)
    def user_profile20():
        return render_template('user-collection8756.html')

    @app.route('/user-collectiona9d9.html', strict_slashes=False)
    def user_profile21():
        return render_template('user-collectiona9d9.html')

    @app.route('/user-collectionafcd.html', strict_slashes=False)
    def user_profile22():
        return render_template('user-collectionafcd.html')

    @app.route('/user-collectionb47b.html', strict_slashes=False)
    def user_profile23():
        return render_template('user-collectionb47b.html')

    @app.route('/user-collectionb59a.html', strict_slashes=False)
    def user_profile24():
        return render_template('user-collectionb59a.html')

    @app.route('/user-collectionbae7.html', strict_slashes=False)
    def user_profile25():
        return render_template('user-collectionbae7.html')

    @app.route('/user-collectionc2cc.html', strict_slashes=False)
    def user_profile26():
        return render_template('user-collectionc2cc.html')

    @app.route('/user-collectionca81.html', strict_slashes=False)
    def user_profile27():
        return render_template('user-collectionca81.html')

    @app.route('/user-collectionda83.html', strict_slashes=False)
    def user_profile28():
        return render_template('user-collectionda83.html')

    @app.route('/user-collectioneb05.html', strict_slashes=False)
    def user_profile29():
        return render_template('user-collectioneb05.html')

    @app.route('/user-collectionf83d.html', strict_slashes=False)
    def user_profile30():
        return render_template('user-collectionf83d.html')

    @app.route('/user-collectionfd6b.html', strict_slashes=False)
    def user_profile31():
        return render_template('user-collectionfd6b.html')


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
