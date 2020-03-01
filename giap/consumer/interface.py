from abc import ABC, abstractmethod
from typing import Any, Dict

from .enums import Method


class ConsumerInterface(ABC):
    def __init__(self, base_url: str):
        if base_url.endswith("/"):
            raise ValueError(
                f"The base URL should not end with a slash, received '{base_url}'"
            )

        self.base_url: str = base_url

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
