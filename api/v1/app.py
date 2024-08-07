#!/usr/bin/python3
"""An app handler 
"""

from models import storage
from app.v1.views import app_views
from os import getenv
from flask import Flask, jsonify, make_response


app = Flask(__name__)
app.register_blueprint(app_views)
@app.teardown_appcontext
def handle_closeStorage():
    """This method calls storage.close"""
    storage.close()

@app.errorhandler(404)
def handler_404():
    """error handler that handles 404 error
    """
    return jsonify({"error": "Not found"}, 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    
    app.run(host, int(port), threaded=True)
