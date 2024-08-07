#!/usr/bin/python3
""" new view for Amenity objects that handles 
all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/api/v1/amenities', methods=['GET'], strict_slashes=False)
def retrieve():
    """Retrieves the list of all amenity objects"""
    all_amenities = storage.sll(Amenity).values()
    list_amenities = []
   
    for i in all_amenities:
        list_amenities.append(i.to_dict)
    return jsonify(list_amenities)

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def amenity_ID(amenity_id):
    """ Retrieves a amenity object by it id"""
    amenityID = storage.get(Amenity, amenity_id)
    if not amenity_ID:
        abort(404)
    return jsonify(amenityID.to_dict())
    
@app_views.route('/api/v1/amenities/<amenity_id>', methods=['DELETE'], 
                 strict_slashes=True) 
def delete(amenity_id):
    """Deletes a amenity object by id"""
    del_amenity = storage.get(Amenity, amenity_id)
    if not del_amenity:
        abort(404)
    storage.delete(del_amenity)
    storage.save()
    return make_response(jsonify({}),200) 
 
@app_views.route('/api/v1/amenities', methods=['POST'], 
                 strict_slashes=True)   
def create():
    """Creates a amenity

    Returns:
        Returns the new amenity with the status code 201
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "name" not in request.get_json():
        abort(400, description="Missing name")
    
    req_json = request.get_json()
    obj = Amenity(**req_json)
    obj.save()
    return make_response(jsonify(obj.to_dict()), 201)

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['PUT'], 
                 strict_slashes=True)
def update(amenity_id):
    """
    Updates a amenity object by id
    """  
    if not request.get_json():
        abort(400, description="Not a JSON")
  
    ignore = ['id', 'created_at', 'updated_at']
    
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(400)
        
    info = request.get_json()        
    for key, value in info.items():
        if key not in ignore:
            setattr(amenity, key, value)
        storage.save()
        return make_response(jsonify(amenity()), 200)