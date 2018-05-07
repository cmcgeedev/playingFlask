from core import DbCore
from playingFlask.src.api.services.baseService import BaseService
import DbCommands as commands

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
        return DbCore()

    def insert_pet(self, pet_info):
        insert_command = commands.INSERT_PET
        insert_values = pet_info['Age'], pet_info['Height'], pet_info['Weight'], pet_info['Breed'], \
            pet_info['species'], pet_info['shelter_id']
        self.db_response = self._db_connection.update_in_table(insert_command, insert_values)

    def update_pet(self, pet_info):
        update_command = commands.UPDATE_PET
        update_values = pet_info['Age'], pet_info['Height'], pet_info['Weight'], pet_info['Breed'], \
            pet_info['species'], pet_info['shelter_id']
        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def get_pet(self, pet_id):
        query = commands.GET_PET_DETAILS
        query_values = pet_id,
        self.db_response = self._db_connection.get_from_table(query, query_values)

    def deactivate_pet(self, pet_id):
        update_command = commands.DEACTIVATE_PET
        update_values = pet_id,
        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def activate_pet(self, pet_id):
        update_command = commands.ACTIVATE_PET
        update_values = pet_id,
        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def get_pets_with_search_criteria(self, search_criteria):

        query = commands.PET_SEARCH_BASIS
        #convert search model to dict
        field_map = vars(search_criteria)

        for key, value in field_map.iteritems():
            #check that vlaue has been set
            if value:
                query += " AND"+" "+key+" = %s"

        query_values = tuple(field_map.values())
        self.db_response = self._db_connection.get_from_table(query, query_values)

