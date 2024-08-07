#!/usr/bin/python3
""" Init file for views.v1"""

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from views.states import *
from views.cities import *
from views.amenities import *
from views.user import *
from views.places_reviews import *