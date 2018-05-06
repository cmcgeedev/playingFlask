import abc


class petBase(object):
    __metaclass__ = abc.ABCMeta
    """
    props
    """

    @abc.abstractproperty
    def id(self):
        return

    @abc.abstractproperty
    def shelter_id(self):
        return

    @abc.abstractproperty
    def height(self):
        return

    @abc.abstractproperty
    def weight(self):
        return

    @abc.abstractproperty
    def age(self):
        return

    @abc.abstractproperty
    def species(self):
        return
    """
    Getters
    """
    @id.getter
    def id(self):
        return

    @shelter_id.getter
    def shelter_id(self):
        return

    @height.getter
    def height(self):
        return

    @weight.getter
    def weight(self):
        return

    @age.getter
    def age(self):
        return

    @species.getter
    def species(self):
        return
    """
    Setters
    """

    @id.setter
    def id(self, id_input):
        return

    @shelter_id.setter
    def shelter_id(self, shelter_id_input):
        return

    @height.setter
    def height(self, height_input):
        return

    @weight.setter
    def weight(self, weight_input):
        return

    @age.setter
    def age(self, age_input):
        return

    @species.setter
    def species(self, species_input):
        return

