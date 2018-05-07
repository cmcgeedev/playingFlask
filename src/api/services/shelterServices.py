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
        self.__db_connection = self.initialize_db_connection()

    def initialize_db_connection(self):
        return DbCore()

    def get_shelter(self, shelter_id):
        query = commands.GET_SHELTER_WITH_ID
        query_values = shelter_id,
        self.db_response = self.__db_connection.update_in_table(query, query_values)


    def get_shelter_with_search_criteria(self, search_criteria):

        query = commands.SHELTER_SEARCH_BASIS
        #convert search model to dict
        field_map = vars(search_criteria)

        for key, value in field_map.iteritems():
            #check that vlaue has been set
            if value:
                query += " AND"+" "+key+" = %s"

        query_values = tuple(field_map.values())
        self.db_response = self.__db_connection.get_from_table(query, query_values)

    def update_shelter(self, shelter_info):
        update_command = commands.UPDATE_SHELTER
        update_values = shelter_info['City'], shelter_info['Is_Active'], shelter_info['Address'], \
            shelter_info['Name'], shelter_info['Capacity']

        self.db_response = self.__db_connection.update_in_table(update_command, update_values)

    def deactivate_shelter(self, shelter_id):
        update_command = commands.ACTIVATE_SHELTER
        update_values = shelter_id,
        self.db_response = self.__db_connection.update_in_table(update_command, update_values)

    def activate_shelter(self, shelter_id):
        update_command = commands.DEACTIVATE_SHELTER
        update_values = shelter_id,
        self.db_response = self.__db_connection.update_in_table(update_command, update_values)

    def insert_shelter(self, shelter_info):
        insert_command = commands.INSERT_PET
        insert_values = shelter_info['City'], shelter_info['Is_Active'], shelter_info['Address'], \
            shelter_info['Name'], shelter_info['Capacity']

        self.db_response = self.__db_connection.update_in_table(insert_command, insert_values)