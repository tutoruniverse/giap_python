from abc import ABC, abstractmethod
from typing import Any, Dict

from .enums import Method


class ConsumerInterface(ABC):
    __slots__ = ("base_url",)

    @abstractmethod
    def send(
        self,
        endpoint: str,
        data: Dict[str, Any],
        token: str,
        *,
        method: Method = Method.POST,
    ):
        pass
