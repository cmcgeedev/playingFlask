from petBase import petBase as Base
from playingFlask.src.api.common.Utilities import validate_required_fields


class pet:
    __required_fields = ['age', 'weight', 'shelter_id', 'height', 'is_active', 'breed', 'species', 'id']

    def __init__(self, payload):
        try:
            field_check = validate_required_fields(self.__required_fields, payload)
            assert field_check
        except AssertionError:
            print 'Required Field Mismatch'
            return
        self.id = payload['id']
        self.age = payload['age']
        self.weight = payload['weight']
        self.shelter_id = payload['shelter_id']
        self.height = payload['height']
        self.is_active = payload['is_active']
        self.breed = payload['breed']
        self.species = payload['species']