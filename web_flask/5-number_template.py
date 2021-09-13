#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
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
def hello_c(text):
    """
    display “C ” followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def hello_python(text='is cool'):
    """
    display “Python ”, followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def hello_number(n):
    """
    display “n is a number” only if n is an integer
    """
    n = int(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template_number(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
