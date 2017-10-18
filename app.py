# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:25:20 2017

@author: Sarai
"""

from random import randint
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    # Return words of affirmation
    quotes = [ "Hello, gorgeous",
               "You look good today",
               "You are valued, and you are worthy",
               "You're appreciated"  ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]
    
    return quote

if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=1313)
    app.run()