from flask_peewee.db import Database
from peewee import DateTimeField, CharField, AutoField, ForeignKeyField, SmallIntegerField
import datetime 
from app import db 

class Locations(db.Model): 
  id = AutoField()
  city = CharField(null=False)
  country = CharField(null=False)
  country_code = CharField(max_length=2)

class Switches(db.Model): 
  id = AutoField() 
  alias = CharField() 
  port_count = SmallIntegerField(null=False)
  location = ForeignKeyField(Locations) 

class Ports(db.Model):
  id = AutoField()
  interface_name = CharField(null=False) 
  ipv6 = CharField(null=False)
  creation_time = DateTimeField(null=False, default=datetime.datetime.now)
  port = SmallIntegerField(null=False)
  switch = ForeignKeyField(Switches, null=False) 