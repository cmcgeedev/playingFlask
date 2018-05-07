from playingFlask.src.api.common.Utilities import validate_required_fields


class PetControllerSearch:

    __required_fields = ['age_min', 'age_max', 'weight_min', 'weight_max', 'user_longitude', 'user_latitude',
                         'max_distance', 'breed', 'species']

    def __init__(self, payload):
        try:
            field_check = validate_required_fields(self.__required_fields, payload)
            if not field_check:
                raise AttributeError
        except AttributeError:
            print 'field check failed'
            return

        self.age_min = payload['age_min']
        self.age_max = payload['age_max']
        self.weight_min = payload['weight_min']
        self.weight_max = payload['weight_max']
        self.user_longitude = payload['user_longitude']
        self.user_latitude = payload['user_latitude']
        self.max_distance = payload['max_distance']
        self.breed = payload['breed']
        self.species = payload['species']


class ShelterControllerSearch:

    __required_fields = ['name', 'city']

    def __init__(self, payload):
        try:
            field_check = validate_required_fields(self.__required_fields, payload)
            if not field_check:
                raise AttributeError
        except AttributeError:
            print 'field check failed'
            return

        self.name = payload['name']
        self.city = payload['city']


class UserLoginRequest:

    __required_fields = ['username', 'password', 'id']

    def __init__(self, payload):
        try:
            field_check = validate_required_fields(self.__required_fields, payload)
            if not field_check:
                raise AttributeError
        except AttributeError:
            print 'field check failed'
            return

        self.id = payload['id']
        self.password = payload['password']
        self.username = payload['username']





