import os
from flask import Flask, Blueprint
from flask_restful import Api


def create_app():
    """
    Initialize the core application.
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))

    with app.app_context():
        # Create and register the blueprints with the app:
        api_blueprint = get_api_blueprint(app)
        app.register_blueprint(api_blueprint, url_prefix="/api")
        return app


def get_api_blueprint(app: Flask) -> Blueprint:
    """
    Responsible for setting up the API Blueprint and all API Resources under it 
    for the application.
    :return: Configured Blueprint object.
    """
    from app.resources.HealthCheck import HealthCheck
    from app.resources.Message import Message

    api_blueprint = Blueprint("api", __name__)
    api = Api(api_blueprint)
    
    api.add_resource(HealthCheck, '/ping')
    api.add_resource(Message, '/message')

    return api_blueprint
