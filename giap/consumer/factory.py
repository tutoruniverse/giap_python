from .implementations.base import Consumer
from .interface import ConsumerInterface


def get_consumer(base_url: str) -> ConsumerInterface:
    return Consumer(base_url)
