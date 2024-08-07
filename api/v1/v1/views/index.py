#!/usr/bin/python3
"""An index file for v1.views"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    """
    returns a JSON: "status": "OK
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def obj_nums():
    """
    an endpoint that retrieves number of objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})