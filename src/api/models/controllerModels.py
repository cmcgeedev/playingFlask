from playingFlask.src.api.common.Utilities import validate_required_fields


class PetControllerSearch:

    __required_fields = ['age_min', 'age_max', 'weight_min', 'weight_max', 'user_longitude', 'user_latitude',
                         'max_distance', 'breed', 'species']

    def __init__(self, payload):
        try:
            assert validate_required_fields(self.__required_fields, payload)
        except AssertionError:
            print 'field check failed'
            return

        self.__age_min = payload['age_min']
        self.__age_max = payload['age_max']
        self.__weight_min = payload['weight_min']
        self.__weight_max = payload['weight_max']
        self.__user_longitude = payload['user_longitude']
        self.__user_latitude = payload['user_latitude']
        self.__max_distance = payload['max_distance']
        self.__breed = payload['breed']
        self.__species = payload['species']


class ShelterControllerSearch:

    __required_fields = ['longitude', 'latitude']

    def __init__(self, payload):
        try:
            assert validate_required_fields(self.__required_fields, payload)
        except AssertionError:
            print 'field check failed'
            return



