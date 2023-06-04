#!/usr/bin/python3
"""An instance of Flask"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ

# Creating an instance of Flask
app = Flask(__name__)

# Registering the blueprint app_views to the Flask instance
app.register_blueprint(app_views)


# Defining a method to handle teardown of the Flask app
@app.teardown_appcontext
def teardown_app_context(exception):
    """Close the storage connection"""
    storage.close()


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, threaded=True)
