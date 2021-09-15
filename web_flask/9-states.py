#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states/<id>')
@app.route('/states', strict_slashes=False)
def states_id(id=None):
    """
        method to render states
    """
    states = storage.all(State)
    if id is not None:
        id = "State." + id
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """
        method to handle teardown
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
