from flask import Flask
from config import Config 
from flask_peewee.db import Database

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
db = Database(app)
