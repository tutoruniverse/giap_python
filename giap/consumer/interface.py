from abc import ABC, abstractmethod

from .enums import Method


class ConsumerInterface(ABC):
    def __init__(self, base_url):
        if base_url.endswith("/"):
            raise ValueError(
                "The base URL should not end with a slash, received '{base_url}'".format(base_url=base_url)
            )

        self.base_url = base_url

    @abstractmethod
    def send(self, endpoint, data, token, *, method=Method.POST):
        pass
