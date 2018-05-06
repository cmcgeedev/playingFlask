import abc


class petBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def height(self):
        return

    @height.setter
    def height(self, height_val):
        return

    @abc.abstractproperty
    def weight(self):
        return

    @weight.setter
    def weight(self, height_val):
        return


    @abc.abstractproperty
    def age(self):
        return

    @age.setter
    def age(self, age_val):
        return

    @abc.abstractproperty
    def species(self):
        return

    @species.setter
    def species(self, breed_val):
        return

    @abc.abstractproperty
    def Id(self):
        return

    @Id.setter
    def Id(self, height_val):
        return
