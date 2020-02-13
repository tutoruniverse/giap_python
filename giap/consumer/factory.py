from . import ConsumerInterface
from .implementations.base import Consumer


def get_consumer() -> ConsumerInterface:
    return Consumer()
