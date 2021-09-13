#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
import sys
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    print Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    print HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello():
    """
    print HBNB
    """
    sys.argv[1].replace("_", " ")
    return 'C{}'.format(sys.argv[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
