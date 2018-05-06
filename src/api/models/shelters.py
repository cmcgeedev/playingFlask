from users import user

class Shelter:
    __location = (0,0)
    __id = ''
    __capacity = 0

    def __init__(self):
        pass
    #props
    @property
    def location(self):
        return self.__location

    @property
    def id(self):
        return self.__id

    @property
    def capacity(self):
        return self.__capacity

    #Getters
    @location.getter
    def location(self):
        return self.__location

    @id.getter
    def id(self):
        return self.__id

    @capacity.getter
    def id(self):
        return self.__capacity

    #setters

    @location.setter
    def location(self, location_input):
        self.__location = location_input

    @capacity.setter
    def capacity(self, capacity_input):
        self.__capacity = capacity_input
