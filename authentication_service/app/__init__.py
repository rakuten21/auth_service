from flask import Flask
from .config import Config
from .database import init_db
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    init_routes(app)

    return app