from typing import Any, Dict

import requests

from giap.errors import ConsumerError
from ..enums import Method
from ..interface import ConsumerInterface


class Consumer(ConsumerInterface):
    @property
    def base_url(self) -> str:
        return ""

    def send(
        self,
        endpoint: str,
        data: Dict[str, Any],
        token: str,
        method: Method = Method.POST,
    ):
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = requests.request(method.value, url, json=data, headers=headers)

            response.raise_for_status()
        except requests.RequestException as e:
            raise ConsumerError(f"Could not send {data} to {endpoint}") from e
