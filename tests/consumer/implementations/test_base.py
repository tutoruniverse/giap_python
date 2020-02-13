import pytest
from requests.exceptions import RequestException

from giap.consumer import Endpoint
from giap.consumer.implementations.base import Consumer
from giap.errors import ConsumerError


def test_base_consumer(mocker):
    mock_request = mocker.patch("giap.consumer.implementations.base.requests.request")

    consumer = Consumer()
    data = {}
    token = "mock token"

    consumer.send(Endpoint.EVENT, data, token)

    mock_request.assert_called_once_with(
        "post",
        f"{consumer.base_url}{Endpoint.EVENT.value}",
        json=data,
        headers={"Authorization": f"Bearer {token}"},
    )


def test_base_consumer_error(mocker):
    mocker.patch(
        "giap.consumer.implementations.base.requests.request",
        side_effect=RequestException,
    )

    consumer = Consumer()
    data = {}
    token = "mock token"

    with pytest.raises(ConsumerError) as exc_info:
        consumer.send(Endpoint.EVENT, data, token)

    assert exc_info.value.message.startswith("Could not send")
