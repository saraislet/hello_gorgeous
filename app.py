# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:25:20 2017

@author: Sarai
"""

from random import randint
from flask import Flask, render_template

app = Flask(__name__)

quotes = [ "Hello, gorgeous",
           "You look good today",
           "You are valued, and you are worthy",
           "You do good work",
           "You can do the thing",
           "You inspire people",
           "You rock",
           "You're appreciated",
           "You're admired",
           "You are powerful",
           "You are capable",
           "You are brilliant",
           "You are loved",
           "You are fun",
           "You make good things happen",
           "You make a difference",
           "Your words and actions are meaningful",
           "Your opinion matters",
           "I believe in you"]


@app.route("/")
def main():
    # Return words of affirmation
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]
    
    return quote + "/n"


@app.route("/hello")
def hello():
    # Return words of affirmation
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]
    
    return render_template('hello.html', quote=quote)


if __name__ == "__main__":
    app.run()