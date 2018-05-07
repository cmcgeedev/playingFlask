from core import DbCore
from baseService import BaseService
import DbCommands as commands


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
        return DbCore()

    def get_shelters_by_city(self, city):
        query = commands.GET_SHELTERS_BY_CITY
        query_values = city,
        response = self._db_connection.get_from_table(query, query_values)

        return response

    def get_shelter_by_id(self, id):
        query = commands.GET_SHELTER_WITH_ID
        query_values = id,
        response = self._db_connection.get_from_table(query, query_values)

        return response

    def update_shelter(self):
        pass

    def delete_shelter(self):
        pass

    def add_shelter(self):
        pass