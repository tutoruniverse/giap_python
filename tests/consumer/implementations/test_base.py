import pytest
from hypothesis import given
from hypothesis import strategies as st
from requests.exceptions import RequestException

from giap.consumer.implementations.base import Consumer
from giap.errors import ConsumerError


@given(
    st.text().map(lambda t: "/{t}".format(t=t)), st.dictionaries(st.text(), st.text()), st.text()
)
def test_base_consumer(mocker, endpoint, data, token):
    mock_request = mocker.patch("giap.consumer.implementations.base.requests.request")

    consumer = Consumer("")

    consumer.send(endpoint, data, token)

    mock_request.assert_called_once_with(
        "post",
        "{}{}".format(consumer.base_url,endpoint),
        json=data,
        headers={"Authorization": "Bearer {}".format(token)},
    )


@given(
    st.text().map(lambda t: "/{t}".format(t=t)), st.dictionaries(st.text(), st.text()), st.text()
)
def test_base_consumer_error(mocker, endpoint, data, token):
    mocker.patch(
        "giap.consumer.implementations.base.requests.request",
        side_effect=RequestException,
    )

    consumer = Consumer("")

    with pytest.raises(ConsumerError) as exc_info:
        consumer.send(endpoint, data, token)

    assert exc_info.value.message.startswith("Could not send")
