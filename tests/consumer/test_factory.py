import pytest

from giap.consumer.factory import get_consumer
from giap.consumer.implementations.base import Consumer


def test_get_consumer():
    consumer = get_consumer("http://localhost:8080")

    assert isinstance(consumer, Consumer)


def test_get_consumer_invalid_base_url():
    with pytest.raises(ValueError):
        get_consumer("http://localhost:8080/")
