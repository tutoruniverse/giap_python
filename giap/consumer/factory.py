from .implementations.base import Consumer


def get_consumer(base_url):
    return Consumer(base_url)
