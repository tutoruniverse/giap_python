from abc import ABC, abstractmethod
from typing import Any, Dict

from .enums import Endpoint, Method


class ConsumerInterface(ABC):
    __slots__ = ("base_url",)

    @abstractmethod
    def send(
        self,
        endpoint: Endpoint,
        data: Dict[str, Any],
        token: str,
        method: Method = Method.POST,
    ):
        pass
