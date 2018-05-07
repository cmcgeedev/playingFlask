from flask_restful import abort, Resource
from playingFlask.src.api.services.shelterServices import ShelterServices
from flask import jsonify, Flask, request, make_response


class ShelterController(Resource):
    def post(self):
        payload = request.get_json()

    def get(self, longitude, latitude):
        shelter_db_connection = ShelterServices.get_shelters_by_location(longitude, latitude)

"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"shelters": [... shelter data]}}
{"type": "insert", "body": {"shelters": [... shelter data]}}

"""