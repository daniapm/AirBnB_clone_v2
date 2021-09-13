#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
    Teardown events abort
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Display a HTML page
    """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
