from petBase import petBase as Base


class MammalGeneric(Base):

    __id = ''
    __shelter_id = ''
    __species = 'Cat'
    __age = ''
    __weight = ''
    __height = ''
    __breed = ''

    def __init__(self):
        pass

    """
    Props
    """
    @property
    def id(self):
        return self.__id

    @property
    def shelter_id(self):
        return self.__shelter_id

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @property
    def height(self):
        return self.__height

    @property
    def breed(self):
        return self.__breed
    """
    Getters
    """
    @id.getter
    def id(self):
        return self.__id

    @shelter_id.getter
    def shelter_id(self):
        return self.__shelter_id

    @species.getter
    def species(self):
        return self.__species

    @age.getter
    def age(self):
        return self.__age

    @weight.getter
    def weight(self):
        return self.__weight

    @height.getter
    def height(self):
        return self.__height

    @breed.getter
    def breed(self):
        return self.__breed

    """
    Setters
    """
    @id.setter
    def id(self, id_input):
        self.__id = id_input

    @shelter_id.setter
    def shelter_id(self, shelter_id_input):
        return self.__shelter_id

    @height.setter
    def height(self, height_input):
        self.__height = height_input

    @weight.setter
    def weight(self, weight_input):
        self.__weight = weight_input

    @age.setter
    def age(self, age_input):
        self.__age = age_input

    @species.setter
    def species(self, species_input):
        self.__species = species_input

    @breed.setter
    def breed(self, breed_input):
        self.__breed = breed_input


class DogGeneric(MammalGeneric):
    def __init__(self):
        super(DogGeneric, self).__init__()


class CatGeneric(MammalGeneric):
    def __init__(self):
        super(CatGeneric, self).__init__()
