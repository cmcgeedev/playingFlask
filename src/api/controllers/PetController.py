from flask_restful import abort, Resource
from playingFlask.src.api.services import petServices
from flask import jsonify, Flask, request, make_response


class PetController(Resource):
    def post(self, pet_id):
        payload = request.get_json()

    def get(self, pet_id):
        pass

class PetSearchController(Resource):
    def post(self):
        payload = request.get_json()

"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"pets": [... pet data]}}
{"type": "insert", "body": {"pets": [... pet data]}}

"""
