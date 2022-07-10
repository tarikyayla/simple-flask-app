import os 

class Config:
  DATABASE = { # https://stackoverflow.com/a/10786663/15307434
    'engine': 'peewee.PostgresqlDatabase',
    'name': "port_list",
    'user': "tarik",
    'host': os.environ.get("DB_HOST", "localhost"),
    'port': 5432,
  }
  FLASK_PORT = os.environ.get("FLASK_PORT", 5000)
  FLASK_DEBUG = os.environ.get("FLASK_DEBUG", True)