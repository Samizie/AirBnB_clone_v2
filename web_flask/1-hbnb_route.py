#!/usr/bin/python3
"""A Module that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handles hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
