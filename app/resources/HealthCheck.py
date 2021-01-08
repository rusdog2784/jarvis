"""
/ping endpoint.
"""
from flask_restful import Resource


class HealthCheck(Resource):
    """
    Health check Resource to notify if the app is alive.
    """

    def get(self):
        return {"message": "This application is alive!"}
