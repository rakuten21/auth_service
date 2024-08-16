from flask import Blueprint
from app.auth.views import auth_blueprint

def init_routes(app):
    app.register_blueprint(auth_blueprint)