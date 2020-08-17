import requests

from giap.errors import ConsumerError
from ..enums import Method
from ..interface import ConsumerInterface


class Consumer(ConsumerInterface):
    def send(self, endpoint, data, token, method=Method.POST):
        url = "{base_url}{endpoint}".format(base_url=self.base_url, endpoint=endpoint)
        headers = {"Authorization": "Bearer {token}".format(token=token)}

        try:
            response = requests.request(method.value, url, json=data, headers=headers)

            response.raise_for_status()
        except requests.RequestException:
            raise ConsumerError("Could not send {data} to {endpoint}".format(data=data, endpoint=endpoint))
