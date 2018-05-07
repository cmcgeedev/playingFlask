from core import DbCore
from baseService import BaseService
import DbCommands as commands


class UserServices(BaseService):

    __db_response = {}

    @property
    def db_response(self):
        return

    @db_response.getter
    def db_response(self):
        return self.__db_response

    @db_response.setter
    def db_response(self, db_response_val):
        self.__db_response = db_response_val

    def __init__(self):
        self.__db_connection = self.initialize_db_connection()
        self.authenticate_user = False

    def initialize_db_connection(self):
        return DbCore()

    def login(self, login_request):
        self.db_response = self.__db_connection.get_user(login_request.id)
        self.authenticate_user = self.__validate_user_credentials(login_request, self.db_response)

    def __validate_user_credentials(self, login_request, user_object):
        try:
            password_match = login_request.password == user_object.password
            username_match = login_request.username == user_object.username
            return password_match and username_match
        except:
            print 'problem authenticating user'
            return False

    def get_user_info(self, user_id):
        query = commands.GET_USER_WITH_ID
        query_values = user_id,
        response = self.__db_connection.get_from_table(query, query_values)
        return response

    def update_user_field(self, user_input):
        if user_input['field'] != 'is_active':
            update_command = commands.UPDATE_USER_FIELD
            update_values = user_input['field'], user_input['value'], user_input['id']
            self.db_response = self.__db_connection.update_in_table(update_command, update_values)
        else:
            self.db_response = {"Error": 'Must Use User Activation Methods' }

    def deactivate_user(self, user_id):
        update_command = commands.DEACTIVATE_USER
        update_values = user_id,
        self.db_response = self.__db_connection.update_in_table(update_command, update_values)

    def activate_user(self, user_id):
        update_command = commands.ACTIVATE_USER
        update_values = user_id,
        self.db_response = self.__db_connection.update_in_table(update_command, update_values)

    def add_user(self, user_info):
        pass