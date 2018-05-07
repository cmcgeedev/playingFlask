from playingFlask.src.api.common.Utilities import validate_required_fields


class Shelter:
    __required_fields = ['city', 'id', 'capacity', 'name', 'address', 'is_active']

    def __init__(self, payload):
        try:
            field_check = validate_required_fields(self.__required_fields, payload)
            if not field_check:
                raise AttributeError
        except AttributeError:
            print 'Missing Required Fields For Shelter - exiting'
            return

        #self.longitude = payload['longitude'] -- not messing with geolocation for now
        #self.latitude = payload['latitude']

        self.city = payload['city']
        self.id = payload['id']
        self.capacity = payload['capacity']
        self.name = payload['name']
        self.address = payload['address']
        self.is_active = payload['is_active']