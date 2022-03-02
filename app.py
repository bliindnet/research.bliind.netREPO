######################################################
## Set up the libraries needed.


import os

# for working with SQL Databases
from cs50 import SQL

# for working with Flask
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
# Not sure what this does
from tempfile import mkdtemp
from matplotlib import animation
from werkzeug.security import check_password_hash, generate_password_hash

# these are functions that I have written
from my_helper_functions import lpm_random, test, usd

#########################################################

# Configure application to connect to flask server
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter (dont know what this does)
# does something like allows you to write 'usd' in jinja
# code...
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# This is a simple function
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test-python")
def testpython():
    animal = lpm_random()
    return render_template("test-python.html", animal=animal)
    


