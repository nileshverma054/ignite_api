from constants import FLASK_APP_NAME
from flask import Flask
from utils.init_utils import create_restful_api

def create_app():
    app = Flask(FLASK_APP_NAME)
    create_restful_api(app)
    return app

main_app = create_app()

if __name__ == "__main__":
    main_app.run(port=5252, debug=True)

