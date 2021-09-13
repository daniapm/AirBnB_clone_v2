#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_request(self):
    """
    This gets called after each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    display a HTML page only if n is an integer
    """
    states = storage.all('State').values() 
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)