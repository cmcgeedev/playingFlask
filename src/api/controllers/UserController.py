from flask_restful import abort, Resource
from flask import jsonify, Flask, request, make_response
import json
from playingFlask.src.api.services.userServices import UserServices
from playingFlask.src.api.models.controllerModels import UserLoginRequest
from playingFlask.src.api.models.users import User


class UserController(Resource):
    def post(self, user_id):
        payload = request.get_json()
        user_info = payload['body']
        user_db_connection = UserServices()

        if payload['type'] == 'update':
            user_model = User(user_info)
            user_db_connection.update_user(user_model)

        if payload['type'] == 'insert':
            user_model = User(user_info)
            user_db_connection.insert_user(user_model)

        if payload['type'] == 'activate':
            user_db_connection.activate_user(user_id)

        if payload['type'] == 'deactivate':
            user_db_connection.deactivate_user(user_id)

        return user_db_connection.db_response

    def get(self, user_id):
        user_db_connection = UserServices()
        user_db_connection.get_user_details(user_id)
        return user_db_connection.db_response


class HelloWorld(Resource):
    def get(self):
        return json.dumps({'Response': 'success'}), 200


class UserSignIn(Resource):
    def post(self, user_id):
        payload = request.get_json()
        user_info = payload['body']
        user_db_connection = UserServices()
        user_login_request = UserLoginRequest(user_info)
        user_db_connection.login(user_login_request)

        return user_db_connection.db_response


"""
Payload types:

{"type": "search", "body": {....search body}}
{"type": "update", "body": {"users": [... user data]}}
{"type": "insert", "body": {"users": [... user data]}}

"""