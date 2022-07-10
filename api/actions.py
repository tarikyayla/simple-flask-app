from flask import Blueprint, jsonify, request
from models import Locations 
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS

api = Blueprint("api", __name__) 
CORS(api)

# I didnt want to install pydantic for validation
 # so thats why its pretty easy to break if you insist. 

class QueryParams(object):
  page = 0
  items_per_page = 20
  
  def __init__(self, page, items_per_page):
    self.page = page
    self.items_per_page = items_per_page

  @staticmethod
  def get_from_args(args):
    page = int(args.get("page", 0))
    items_per_page = int(args.get("items-per-page", 20))

    return QueryParams(page, items_per_page)


# first time using peewee, looks pretty cool

@api.route("/locations", methods=["GET"]) 
def get_locations():
  params = QueryParams.get_from_args(request.args);
  data = Locations.select().paginate(params.page, params.items_per_page).order_by(Locations.id).dicts()
  return jsonify(list(data))

@api.route("locations/<id>", methods=["GET"])
def get_location(id: int): 
  location = Locations.get_or_none(Locations.id == id) 

  if location is None:
    return {"ex": f"Location with id {id} not found"}, 404
  return model_to_dict(location)