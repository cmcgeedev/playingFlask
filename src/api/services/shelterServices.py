from core import dbCore
from baseService import BaseService


class ShelterServices(BaseService):

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
        self._db_connection = self.initialize_db_connection()

    def initialize_db_connection(self):
        return dbCore()

    def get_shelters_by_location(self, longitude, latitude):
        pass

    def get_shelter_by_id(self):
        pass

    def update_shelter(self):
        pass

    def delete_shelter(self):
        pass

    def add_shelter(self):
        pass