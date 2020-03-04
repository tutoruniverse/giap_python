import time
from typing import Any, Dict, List, Optional, Union

from giap.consumer import ConsumerInterface, Method, Operation, get_consumer
from giap.meta import __lib_name__, __version__


class GIAP:
    def __init__(self, token: str, base_url: str):
        self._token: str = token
        self._consumer: ConsumerInterface = get_consumer(base_url)

    def track(
        self,
        id_: Union[int, str],
        name: str,
        properties: Dict[str, Any],
        ip_address: Optional[str] = None,
    ):
        endpoint = "/events"

        event_data: Dict[str, Any] = {
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

    def set_profile_properties(self, id_: Union[int, str], properties: Dict[str, Any]):
        endpoint = f"/profiles/{id_}"

        self._consumer.send(endpoint, properties, self._token, method=Method.PUT)

    def increase(
        self, id_: Union[int, str], property_name: str, value: Union[List, int, float]
    ):
        endpoint = f"/profiles/{id_}/{property_name}"
        data = {"operation": Operation.INCREASE, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    def append(
        self, id_: Union[int, str], property_name: str, value: Union[List, int, float]
    ):
        endpoint = f"/profiles/{id_}/{property_name}"
        data = {"operation": Operation.APPEND, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    def remove(
        self, id_: Union[int, str], property_name: str, value: Union[List, int, float]
    ):
        endpoint = f"/profiles/{id_}/{property_name}"
        data = {"operation": Operation.REMOVE, "value": value}
        self._consumer.send(endpoint, data, self._token, method=Method.PUT)

    @property
    def unix_timestamp_in_ms(self) -> int:
        return int(time.time() * 1000)
