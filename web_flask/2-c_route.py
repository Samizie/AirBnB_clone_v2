#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! when route '/' is called """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB when /hbnb route is called """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints the message when /c is called """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
