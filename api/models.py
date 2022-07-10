from peewee import CharField, AutoField
from app import db 

class Locations(db.Model): 
  id = AutoField()
  city = CharField(null=False)
  country = CharField(null=False)
  country_code = CharField(max_length=2)
