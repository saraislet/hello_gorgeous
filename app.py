# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:25:20 2017

@author: Sarai
"""

from random import randint
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
@cross_origin()
def main():
    # Return words of affirmation
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]
    
    return quote + "\n"


@app.route("/hello")
def hello():
    # Return words of affirmation
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]
    
    return render_template('hello.html', quote=quote)


if __name__ == "__main__":
    app.run()


quotes = [ "Hello, gorgeous",
           "You look good today",
           "You are valued, and you are worthy",
           "You do good work",
           "You can change the future",
           "You can do the thing",
           "You can move mountains",
           "You inspire people",
           "You rock",
           "You're appreciated",
           "You're a badass",
           "You are a gem",
           "You are admired",
           "You are amazing",
           "You are brilliant",
           "You are capable",
           "You are fun",
           "You are loved",
           "You are lovely",
           "You are powerful",
           "You are revolutionary",
           "You are smart",
           "You are worth it",
           "You make good things happen",
           "You make a difference",
           "Your opinion matters",
           "Your presence matters",
           "Your presence is valuable",
           "Your words and actions are meaningful",
           "I am proud of you",
           "I believe in you"]
