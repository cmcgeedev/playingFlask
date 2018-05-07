from flask_restful import abort, Resource
from playingFlask.src.api.services.shelterServices import ShelterServices
from flask import jsonify, Flask, request, make_response
from playingFlask.src.api.models.controllerModels import ShelterControllerSearch
from playingFlask.src.api.models.shelters import Shelter


class ShelterController(Resource):
    def post(self, shelter_id):
        payload = request.get_json()
        shelter_info = payload['body']
        shelter_db_connection = ShelterServices()

        if payload['type'] == 'update':
            shelter_model = Shelter(shelter_info)
            shelter_db_connection.update_shelter(shelter_model)

        if payload['type'] == 'insert':
            shelter_model = Shelter(shelter_info)
            shelter_db_connection.insert_shelter(shelter_model)

        if payload['type'] == 'search':
            shelter_search_model = ShelterControllerSearch(shelter_info)
            shelter_db_connection.get_shelter_with_search_criteria(shelter_search_model)

        if payload['type'] == 'activate':
            shelter_db_connection.activate_shelter(shelter_id)

        if payload['type'] == 'deactivate':
            shelter_db_connection.deactivate_shelter(shelter_id)

        return shelter_db_connection.db_response

    def get(self, shelter_id):
        shelter_db_connection = ShelterServices()
        shelter_db_connection.get_shelter(shelter_id)
        return shelter_db_connection.db_response


"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"shelters": [... shelter data]}}
{"type": "insert", "body": {"shelters": [... shelter data]}}

"""