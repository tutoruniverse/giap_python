from typing import Any, Dict

import requests

from giap.errors import ConsumerError

from .. import ConsumerInterface, Endpoint, Method


class Consumer(ConsumerInterface):
    @property
    def base_url(self) -> str:
        return ""

    def send(
        self,
        endpoint: Endpoint,
        data: Dict[str, Any],
        token: str,
        method: Method = Method.POST,
    ):
        url = f"{self.base_url}{endpoint.value}"
        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = requests.request(method.value, url, json=data, headers=headers)

            response.raise_for_status()
        except requests.RequestException as e:
            raise ConsumerError(f"Could not send {data} to {endpoint.value}") from e
