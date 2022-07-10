from app import app 
from config import Config
from actions import api

app.register_blueprint(api, url_prefix="/api") # best to go with versioning tho

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=Config.FLASK_PORT,
            debug=Config.FLASK_DEBUG) 
