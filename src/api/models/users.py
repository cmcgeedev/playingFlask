
class User:

    __is_admin = False
    __id = ''
    __session_id = ''
    __password = ''
    __username = ''

    def __init__(self):
        pass

    @property
    def is_admin(self):
        return self.__is_admin

    @property
    def id(self):
        return self.__id

    @property
    def session_id(self):
        return self.__session_id

    @property
    def password(self):
        return self.__password

    @property
    def username(self):
        return self.__username


