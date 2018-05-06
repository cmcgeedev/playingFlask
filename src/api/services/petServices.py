import SQLAlchemy
from core import dbCore


class PetServices:
    def __init__(self):
        self._db_connection = dbCore()

    def create_pet(self, pet_info):
        table = 'pets'
        query = '' #build from pet_info
        self._db_connection.addToTable(table, query)

    def update_pet(self, pet_info):
        table = 'pets'
        query = '' #build from pet_info
        self._db_connection.updateInTable(table, query)

    def get_pet(self, pet_id):
        table = 'pets'
        query = 'SELECT * FROM pets WHERE Id='+pet_id
        self._db_connection.getFromTable(table, query)

    def get_pets_with_search_criteria(self, search_criteria):
        table = 'pets'
        query = '' #build query from search criteria
        self._db_connection.getFromTable(table, query)

