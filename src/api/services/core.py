import psycopg2
import psycopg2.extras
from credentials import DBHOST, DBNAME, DBPASS, DBUSER


class DbCore:
    def __init__(self):
        self._postgres_connector = PostgresFacade()

    def get_from_table(self, query, query_values):
        response = self._postgres_connector.select_from_table(query, query_values)

        return response

    def update_in_table(self, update_command, update_values):
        response = self._postgres_connector.update_record(update_command, update_values)

        return response

    def delete_from_table(self, delete_command, delete_values):
        response = self._postgres_connector.update_record(delete_command, delete_values)

        return response

    def insert_in_table(self, insert_command, insert_values):
        response = self._postgres_connector.insert_record(insert_command, insert_values)

        return response


class PostgresFacade():

    def __init__(self):
        self.pet_pals_db_connection = psycopg2.connect("dbname='"+DBNAME+"' user='"+DBUSER+"' host='"+DBHOST+"' password='"+
                                           DBPASS+"'")
        self.pet_pals_cursor = self.pet_pals_db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def select_from_table(self, query, query_values):
        self.pet_pals_cursor.execute(query, query_values)
        response = self.pet_pals_cursor.fetchall()
        return response

    def insert_record(self, insert_command, insert_values):
        self.pet_pals_cursor.execute(insert_command, insert_values)
        rows_inserted = self.pet_pals_cursor.rowcount
        self.pet_pals_cursor.execute('COMMIT')

        return rows_inserted

    def update_record(self, update_command, update_values):
        self.pet_pals_cursor.execute(update_command, update_values)
        rows_updated = self.pet_pals_cursor.rowcount
        self.pet_pals_cursor.execute('COMMIT')

        return rows_updated

    #probably don't want this here, but adding anyway
    def delete_record(self, delete_command, delete_values):
        self.pet_pals_cursor.execute(delete_command, delete_values)
        rows_deleted = self.pet_pals_cursor.rowcount
        return rows_deleted

    #to be removed - just for reminding me of the data structure
    def get_table_description(self,table_name):
        self.pet_pals_cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name ='"+table_name+"'")
        columns = self.pet_pals_cursor.fetchall()
        print columns

    def get_table_data(self,table_name):
        self.pet_pals_cursor.execute("SELECT * FROM "+table_name)
        rows = self.pet_pals_cursor.fetchall()
        print self.pet_pals_cursor.description
        for row in rows:
            print dict(row)
        print rows


