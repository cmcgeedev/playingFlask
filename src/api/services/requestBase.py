import abc


class requestBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def endpoint(self):
        return

    @endpoint.setter
    def endpoint(self):
        return

    @abc.abstractproperty
    def headers(self):
        return

    @headers.setter
    def headers(self, messages_input):
        return

    @abc.abstractproperty
    def body(self):
        return

    @body.setter
    def body(self, body_input):
        return

    #map response to
    @abc.abstractproperty
    def responseMapping(self, map_values):
        return

    @abc.abstractmethod
    def transform_messages(self):
        """Logic for  transforming raw SQS messages"""
        return

    @abc.abstractmethod
    def callout_to_service(self):
        """Logic for posting to target service"""
        return

    @abc.abstractmethod
    def format_results(self):
        """Pass results back to SQS fanout lambda"""
        return