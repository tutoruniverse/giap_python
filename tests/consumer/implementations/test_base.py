import pytest
from requests.exceptions import RequestException

from giap.consumer.implementations.base import Consumer
from giap.errors import ConsumerError


def test_base_consumer(mocker):
    mock_request = mocker.patch("giap.consumer.implementations.base.requests.request")

    consumer = Consumer()
    endpoint = "/tests"
    data = {}
    token = "mock token"

    consumer.send(endpoint, data, token)

    mock_request.assert_called_once_with(
        "post",
        f"{consumer.base_url}{endpoint}",
        json=data,
        headers={"Authorization": f"Bearer {token}"},
    )


def test_base_consumer_error(mocker):
    mocker.patch(
        "giap.consumer.implementations.base.requests.request",
        side_effect=RequestException,
    )

    consumer = Consumer()
    endpoint = "/tests"
    data = {}
    token = "mock token"

    with pytest.raises(ConsumerError) as exc_info:
        consumer.send(endpoint, data, token)

    assert exc_info.value.message.startswith("Could not send")
