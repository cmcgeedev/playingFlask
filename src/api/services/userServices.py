from core import dbCore
from baseService import BaseService


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

    def initialize_db_connection(self):
        return dbCore()

    def login(self):
        pass

    def get_user_info(self, user_id):
        pass

    def update_user_info(self, user_info):
        pass

    def deactivate_user(self, user_id):
        pass

    def activate_user(self, user_id):
        pass

    def add_user(self, user_info):
        pass