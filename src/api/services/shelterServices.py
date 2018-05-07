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
        self.db_response = self._db_connection.get_from_table(query, query_values)

    def get_shelter_by_id(self, id):
        query = commands.GET_SHELTER_WITH_ID
        query_values = id,
        self.db_response = self._db_connection.get_from_table(query, query_values)


    def update_shelter(self, shelter_info):
        update_command = commands.UPDATE_SHELTER
        update_values = shelter_info['City'], shelter_info['Is_Active'], shelter_info['Address'], \
            shelter_info['Name'], shelter_info['Capacity']

        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def deactivate_shelter(self, shelter_id):
        update_command = commands.ACTIVATE_SHELTER
        update_values = shelter_id,
        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def activate_shelter(self, shelter_id):
        update_command = commands.DEACTIVATE_SHELTER
        update_values = shelter_id,
        self.db_response = self._db_connection.update_in_table(update_command, update_values)

    def insert_shelter(self, shelter_info):
        insert_command = commands.INSERT_PET
        insert_values = shelter_info['City'], shelter_info['Is_Active'], shelter_info['Address'], \
            shelter_info['Name'], shelter_info['Capacity']

        self.db_response = self._db_connection.update_in_table(insert_command, insert_values)