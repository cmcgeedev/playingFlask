from petBase import petBase as Base

class cat(Base):
    def __init__(self):
        pass
    _id = ''
    _species = 'Cat'
    _age = ''
    _weight = ''
    _height = ''
    _breed = ''
    """
    Props
    """
    @property
    def id(self):
        return self._id

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def breed(self):
        return self._breed
    """
    Getters
    """
    @id.getter
    def id(self):
        return self._id

    @species.getter
    def species(self):
        return self._species

    @age.getter
    def age(self):
        return self._age

    @weight.getter
    def weight(self):
        return self._weight

    @height.getter
    def height(self):
        return self._height

    @breed.getter
    def breed(self):
        return self._breed

    """
    Setters
    """