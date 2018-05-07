from flask_restful import abort, Resource
from playingFlask.src.api.services.petServices import PetServices
from flask import jsonify, Flask, request, make_response
from playingFlask.src.api.models.controllerModels import PetControllerSearch
from playingFlask.src.api.models.pets import Pet


class PetController(Resource):

    def post(self, pet_id):
        payload = request.get_json()
        pet_info = payload['body']
        pet_db_connection = PetServices()
        if payload['type'] == 'update':
            pet_model = Pet(pet_info)
            pet_db_connection.update_pet(pet_model)

        if payload['type'] == 'insert':
            pet_model = Pet(pet_info)
            pet_db_connection.insert_pet(pet_model)

        if payload['type'] == 'activate':
            pet_db_connection.activate_pet(pet_id)

        if payload['type'] == 'deactivate':
            pet_db_connection.deactivate_pet(pet_id)

        if payload['type'] == 'search':
            petSearchModel = PetControllerSearch(payload)
            pet_db_connection.get_pets_with_search_criteria(petSearchModel)

        return pet_db_connection.db_response

    def get(self, pet_id):
        pet_db_connection = PetServices()
        pet_db_connection.get_pet(pet_id)
        return pet_db_connection.db_response

"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"... pet info"}}
{"type": "activate", "body": {} }
{"type": "deactivate", "body": {}}
{"type": "insert", "body": {"...pet info"}}

"""
