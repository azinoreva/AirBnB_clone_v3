#!/usr/bin/python3
"""
Flask app
"""
from os import getenv
from flask import Flask
from models import Storage
from api.v1.views import app_views

app = FLask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_HOST', 5000)
    app.run(host = HOST, port = PORT, threaded = TRUE)

    
