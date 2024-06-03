#!/usr/bin/python3

"""
start the Flask Application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "<p>Hello HBNB!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

