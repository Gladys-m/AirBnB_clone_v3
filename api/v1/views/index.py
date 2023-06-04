#!/usr/bin/python3
""" Index File """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Api Status"""
    return jsonify({'status': 'OK'})
