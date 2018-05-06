import SQLAlchemy

class dbCore:
    def __init__(self):
        pass

    def getFromTable(self, table, query):
        pass

    def updateInTable(self, table, ids, payload):
        pass

    def deleteFromTable(self, table, ids):
        pass

    def addToTable(self, table, query):
        pass


import psycopg2
import psycopg2.extras
from credentials import DBHOST, DBNAME, DBPASS, DBUSER


class PostgresInterface():
    def __init__(self):
        self.pet_pals_db_connection = psycopg2.connect("dbname='"+DBNAME+"' user='"+DBUSER+"' host='"+DBHOST+"' password='"+
                                           DBPASS+"'")
        self.pet_pals_cursor = self.pet_pals_db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        self.user_info_sql = "SELECT * FROM user WHERE Id = (%s)" #"SELECT * FROM list where owner_zuid = %s"

        self.shelter_info_sql = ""
        self.pet_info_sql = ""

    def select_user_lists(self,user_id):
        print self.pet_pals_cursor.mogrify(self.user_info_sql,(user_id,))
        self.pet_pals_cursor.execute(self.user_info_sql,(user_id,))
        lists_data = self.pet_pals_cursor.fetchall()

        return lists_data

    def select_pets_by_breed(self, breed_info):
        self.pet_pals_cursor.execute("")

    def insert_shelter(self,shelter_data):
        self.pet_pals_cursor.execute("INSERT INTO shelters (name,is_active,longitude,latitude, city, "
                                      "zip,created_by,updated_by) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                      shelter_data)

        self.pet_pals_cursor.execute('SELECT LASTVAL()')
        lastid = self.pet_pals_cursor.fetchone()['lastval']
        self.pet_pals_cursor.execute('COMMIT')
        print lastid
        return lastid

    def insert_pet(self,criteria_data):
        self.pet_pals_cursor.execute("INSERT INTO pets (shelter_id,breed,species,"
                                      "age,height,weight)",criteria_data)
        self.pet_pals_cursor.execute('SELECT LASTVAL()')
        lastid = self.pet_pals_cursor.fetchone()['lastval']
        self.pet_pals_cursor.execute("COMMIT")
        return lastid

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



if __name__ == "__main__":
    srt = PostgresInterface()
    srt.get_table_description('pets')
    srt.get_table_description('shelters')
    srt.get_table_description('users')
    print srt.get_table_data("pets")

