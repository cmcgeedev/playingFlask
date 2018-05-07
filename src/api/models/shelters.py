from playingFlask.src.api.common.Utilities import validate_required_fields


class Shelter:
    __required_fields = ['city', 'id', 'capacity']

    def __init__(self, payload):
        try:
            assert validate_required_fields(self.__required_fields, payload)
        except AssertionError:
            print 'Missing Required Fields For Shelter - exiting'
            return

        #self.longitude = payload['longitude'] -- not messing with geolocation for now
        #self.latitude = payload['latitude']

        self.city = payload['city']
        self.id = payload['id']
        self.capacity = payload['capacity']