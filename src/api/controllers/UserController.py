from flask_restful import abort, Resource
from playingFlask.src.api.services import petServices
from flask import jsonify, Flask, request, make_response
import json
from playingFlask.src.api.services.userServices import UserServices


class UserController(Resource):
    def post(self, pet_id):
        payload = request.get_json()

    def get(self, pet_id):
        pass


class HelloWorld(Resource):
    def get(self):
        return json.dumps({'Response': 'success'}), 200

class SignIn(Resource):
    def post(self, user_id, password):
        pass


"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"users": [... user data]}}
{"type": "insert", "body": {"users": [... user data]}}

"""