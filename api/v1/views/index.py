#!/usr/bin/python3
"""
Create  a Flask app view 
"""

fromm flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """ gets api status"""
    response = {'status' : "Ok"}
    return jsonify(response)
