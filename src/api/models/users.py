from playingFlask.src.api.common.Utilities import validate_required_fields


class User:

    __required_fields = ['access_level', 'id', 'session_id', 'password', 'username']

    def __init__(self, payload):

        try:
            assert validate_required_fields(self.__required_fields, payload)
        except AssertionError:
            print 'Missing required fields'

        self.access_level = payload['access_level']
        self.id = payload['id']
        self.session_id = payload['session_id']
        self.password = payload['password']
        self.username = payload['username']

