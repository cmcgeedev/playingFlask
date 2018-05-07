
GET_USER_WITH_ID = "SELECT Id, Username, Password FROM Users WHERE Id = %s"
INSERT_USER = "INSERT INTO Users (Username, Password, City) VALUES (%s, %s)"
UPDATE_USER_FIELD = "UPDATE Users SET (%s) = (%s) WHERE Id = %s"

ACTIVATE_USER = "UPDATE Users SET (is_active) = (True) WHERE Id = %s"
DEACTIVATE_USER = "UPDATE Users SET (is_active) = (False) WHERE Id = %s"

GET_PET_DETAILS = "SELECT Age, Height, Weight, Breed, Species FROM Pets WHERE Id = %s"
PET_SEARCH_BASIS = "SELECT Age, Height, Weight, Breed, Species FROM Pets WHERE is_active = TRUE AND "
INSERT_PET = "INSERT INTO Pets (Age, Height, Weight, Breed, Species, Shelter_id) VALUES (%s, %s, %s, %s, %s, %s)"
UPDATE_PET = "UPDATE Pets SET (Age, Height, Weight, Breed, Species, Shelter_id) = (%s, %s, %s, %s, %s, %s) WHERE Id = %s"
ACTIVATE_PET = "UPDATE Pets SET (Is_Active) = (True) WHERE Id = %s"
DEACTIVATE_PET = "UPDATE Pets SET (Is_Active) = (False) WHERE Id = %s"

SHELTER_SEARCH_BASIS = "SELECT Id, City, Capacity, Address FROM Shelters WHERE Is_Active = TRUE AND "
UPDATE_SHELTER = "UPDATE Shelters (City, Capacity) = (%s, %s)"
ACTIVATE_SHELTER = "UPDATE Shelters SET (Is_Active) = (True) WHERE Id = %s"
DEACTIVATE_SHELTER = "UPDATE Shelters SET (Is_Active) = (False) WHERE Id = %s"
GET_SHELTER_WITH_ID = "SELECT Id, City, Capacity, Address FROM Shelters WHERE Id = %s"