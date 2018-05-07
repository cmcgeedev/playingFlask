
GET_USER_WITH_ID = "SELECT Id, Username, Password FROM Users WHERE Id = %s"
INSERT_USER = "INSERT INTO Users (Username, Password, City) VALUES (%s, %s)"
UPDATE_USER_FIELD = "UPDATE Users SET (%s) = (%s) WHERE Id = %s"

ACTIVATE_USER = "UPDATE Users SET (is_active) = (True) WHERE Id = %s"
DEACTIVATE_USER = "UPDATE Users SET (is_active) = (False) WHERE Id = %s"

GET_PET_DETAILS = "SELECT Age, Height, Weight, Breed, Species FROM Pets WHERE Id = %s"
PET_SEARCH_BASIS = "SELECT Age, Height, Weight, Breed, Species FROM Pets WHERE is_active = TRUE AND "

GET_SHELTER_WITH_ID = "SELECT Id FROM Shelters WHERE Id = %s"
GET_SHELTERS_BY_CITY = "SELECT Id FROM Shelters WHERE City = %s"


"""
        self.pet_pals_cursor.execute("INSERT INTO shelters (name,is_active,longitude,latitude, city, "
                                      "zip,created_by,updated_by) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                      shelter_data)

"""
