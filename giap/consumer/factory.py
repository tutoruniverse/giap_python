from .implementations.base import Consumer
from .interface import ConsumerInterface


def get_consumer() -> ConsumerInterface:
    return Consumer()
