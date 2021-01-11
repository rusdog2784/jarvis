"""
/message endpoint.
"""
from flask import request, Response, jsonify
from flask_restful import Resource
from app.modules.wit_ai import get_wit_analysis


class Message(Resource):
    """
    Resource meant to accept incoming messages that will be processed 
    by Jarvis.
    """

    def post(self):
        try:
            json_data = request.get_json(force=True)
            if not json_data or "text" not in json_data:
                return {"message": "No input data provided or invalid input (must provide 'text')."}, 400
            text = json_data.get("text", None)
            analysis = get_wit_analysis(text)
            return jsonify({
                "message": f"{text}",
                "data": analysis
            })
        except Exception as unknown_exception:
            return jsonify({
                "message": "Unknown Error Occurred",
                "error": f"{unknown_exception}"
            })
