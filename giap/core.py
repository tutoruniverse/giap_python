import time

from giap.consumer import Method, Operation, get_consumer
from giap.meta import __lib_name__, __version__


class GIAP:
    def __init__(self, token, base_url):
        self._token = token
        self._consumer = get_consumer(base_url)

    def track(self, id_, name, properties, ip_address=None, ):
        endpoint = "/events"

        event_data = {
            "$distinct_id": str(id_),
            "$name": name,
            "$time": self.unix_timestamp_in_ms,
            "$lib": __lib_name__,
            "$lib_version": __version__,
        }

        event_data.update(properties)

        if ip_address is not None:
            event_data["$sender_ip"] = ip_address

        self._consumer.send(endpoint, {"events": [event_data]}, self._token)

    def set_profile_properties(self, id_, properties):
        endpoint = "/profiles/{}".format(id_)

        self._consumer.send(endpoint, properties, self._token, method=Method.PUT)

    def increase(self, id_, property_name, value):
        endpoint = "/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name)
        data = {"operation": Operation.INCREASE, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    def append(self, id_, property_name, value):
        endpoint = "/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name)
        data = {"operation": Operation.APPEND, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    def remove(self, id_, property_name, value):
        endpoint = "/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name)
        data = {"operation": Operation.REMOVE, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    @property
    def unix_timestamp_in_ms(self):
        return int(time.time() * 1000)
