from flask_restful import abort, Resource
from playingFlask.src.api.services.petServices import PetServices
from flask import jsonify, Flask, request, make_response
from playingFlask.src.api.models.controllerModels import PetControllerSearch

class PetController(Resource):
    def post(self, pet_id):
        payload = request.get_json()

    def get(self, pet_id):
        pass

class PetSearchController(Resource):
    def post(self):
        payload = request.get_json()
        petSearchModel = PetControllerSearch(payload)
        pet_db_connection = PetServices()
        pet_db_connection.get_pets_with_search_criteria(payload)
        return pet_db_connection.db_response

"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"pets": [... pet data]}}
{"type": "insert", "body": {"pets": [... pet data]}}
{"type": "default", "body": {"error": "Type not set correctly"}}

"""
