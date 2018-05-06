from flask_restful import abort, Resource
from playingFlask.src.api.services import petServices
from flask import jsonify, Flask, request, make_response


class ShelterController(Resource):
    def post(self):
        payload = request.get_json()

    def get(self, pet_id):
        pass

"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"shelters": [... shelter data]}}
{"type": "insert", "body": {"shelters": [... shelter data]}}

"""