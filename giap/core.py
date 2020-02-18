import time
from typing import Any, Dict, Optional, Union

from giap.consumer import ConsumerInterface, Method, get_consumer
from giap.meta import __lib_name__, __version__


class GIAP:
    def __init__(self, token: str):
        self._token: str = token
        self._consumer: ConsumerInterface = get_consumer()

    def track(
        self,
        id_: Union[int, str],
        name: str,
        properties: Dict[str, Any],
        ip_address: Optional[str] = None,
    ):
        endpoint = "/events"

        event_data: Dict[str, Any] = {
            "_distinct_id": str(id_),
            "_name": name,
            "_time": self.unix_timestamp,
            "_lib": __lib_name__,
            "_lib_version": __version__,
        }

        event_data.update(properties)

        if ip_address is not None:
            event_data["_sender_ip"] = ip_address

        self._consumer.send(endpoint, {"events": [event_data]}, self._token)

    def set_profile_properties(self, id_: Union[int, str], properties: Dict[str, Any]):
        endpoint = f"/profiles/{id_}"

        self._consumer.send(endpoint, properties, self._token, method=Method.PUT)

    @property
    def unix_timestamp(self) -> int:
        return int(time.time())
