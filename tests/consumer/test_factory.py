from giap.consumer.factory import get_consumer
from giap.consumer.implementations.base import Consumer


def test_get_consumer():
    consumer = get_consumer()

    assert isinstance(consumer, Consumer)
