from flask import Blueprint, jsonify, request
from models import Locations 
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS

api = Blueprint("api", __name__) 
CORS(api)

@api.route("/locations", methods=["GET"]) 
def get_locations():
  data = Locations.select().order_by(Locations.id).dicts()
  return jsonify(list(data))

@api.route("locations/<id>", methods=["GET"])
def get_location(id: int): 
  location = Locations.get_or_none(Locations.id == id) 

  if location is None:
    return {"ex": f"Location with id {id} not found"}, 404
  return model_to_dict(location)