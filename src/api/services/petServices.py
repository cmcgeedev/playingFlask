import SQLAlchemy
from core import dbCore
from playingFlask.src.api.services.baseService import BaseService


class PetServices(BaseService):

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

    def create_pet(self, pet_info):
        table = 'pets'
        query = '' #build from pet_info
        self.db_response = self._db_connection.add_to_table(table, query)

    def update_pet(self, pet_info):
        table = 'pets'
        ids = '' #grab from pet_info
        query = '' #build from pet_info
        self.db_response = self._db_connection.update_in_table(table, ids, query)

    def get_pet(self, pet_id):
        table = 'pets'
        query = 'SELECT * FROM pets WHERE Id='+pet_id
        self.db_response = self._db_connection.get_from_table(table, query)

    def get_pets_with_search_criteria(self, search_criteria):
        table = 'pets'
        query = '' #build query from search criteria
        self.db_response = self._db_connection.get_from_table(table, query)

