from flask import Blueprint, jsonify, request
from models import Locations, Switches, Ports 
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS

api = Blueprint("api", __name__) 
CORS(api)

# I didnt want to install pydantic for validation
 # so thats why its pretty easy to break if you insist. 

class InvalidQueryParamException(Exception): 
  pass


@api.errorhandler(InvalidQueryParamException)
def invalid_query_param_handler(e):
  return {"ex": "Query param is not valid"}, 400


class QueryParams(object):
  page = 1
  items_per_page = 20
  
  def __init__(self, page, items_per_page):
    self.page = page
    self.items_per_page = items_per_page

  @staticmethod 
  def is_valid_int(value):
    """ too lazy to implement something proper, should work. Might be better to have a validator decorator"""
    try:
      value = int(value)
      if not isinstance(value, int) or value < 0: raise Exception
    except: 
      raise InvalidQueryParamException

    return True


  @staticmethod
  def get_from_args(args):
    page = int(args.get("page", 0))
    items_per_page = int(args.get("items-per-page", 20))

    QueryParams.is_valid_int(page)
    QueryParams.is_valid_int(items_per_page)

    return QueryParams(page, items_per_page)


# first time using peewee, looks pretty cool

@api.route("/locations", methods=["GET"]) 
def get_locations():
  params = QueryParams.get_from_args(request.args);
  data = Locations.select().paginate(params.page, params.items_per_page).order_by(Locations.id).dicts()
  return jsonify(list(data))

@api.route("locations/<id>", methods=["GET"])
def get_location(id: int): 
  QueryParams.is_valid_int(id) 
  location = Locations.get_or_none(Locations.id == id) 

  if location is None:
    return {"ex": f"Location with id {id} not found"}, 404
  return model_to_dict(location)

@api.route("/locations/<id>/switches")
def get_switches(id: int):
  QueryParams.is_valid_int(id)
  params = QueryParams.get_from_args(request.args);
  location = Locations.get_or_none(Locations.id == id) 
  if(location is None):
    return {"ex": f"Switch with id {id} not found"}, 404

  data = Switches.select().where(Switches.location_id == id).paginate(params.page, params.items_per_page).dicts()
  return jsonify(list(data)) 

@api.route("/switches/<id>")
def get_switch(id: int): 
  QueryParams.is_valid_int(id)

  switch = Switches.get_or_none(Switches.id == id) 

  if switch is None:
    return {"ex": f"Switch with id {id} not found"}, 404
  return model_to_dict(switch)


@api.route("/switches/<id>/ports")
def get_ports(id: int):
  QueryParams.is_valid_int(id)
  switch = Switches.get_or_none(Switches.id == id) 
  params = QueryParams.get_from_args(request.args);

  if(switch is None):
    return {"ex": f"Switch with id {id} not found"}, 404

  ports = Ports.select().where(Ports.switch_id == id).paginate(params.page, params.items_per_page).dicts()
  return jsonify(list(ports))