from app import app 
import os 

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=os.environ.get("FLASK_PORT", 5000),
            debug=os.environ.get("FLASK_DEBUG", True)) #TODO: check might need to parse that value into Boolean 
