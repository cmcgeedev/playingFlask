import abc


class BaseService:

    @abc.abstractproperty
    def db_response(self):
        return

    @db_response.getter
    def db_response(self):
        return

    @db_response.setter
    def db_response(self, db_response_val):
        return

    @abc.abstractmethod
    def initialize_db_connection(self):
        return