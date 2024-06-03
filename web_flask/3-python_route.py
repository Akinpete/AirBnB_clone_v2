#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the text variable"""
    parsed_text = text.replace('_', ' ')
    return "C {}".format(parsed_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    parsed_text = text.replace('_', ' ')
    return "Python {}".format(parsed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
