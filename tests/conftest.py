from unittest.mock import Mock

import pytest
from hypothesis import strategies
from hypothesis.strategies import text as _text


@pytest.fixture
def mock_consumer(mocker):
    from giap.consumer import ConsumerInterface

    mock = Mock(spec=ConsumerInterface)

    mocker.patch("giap.core.get_consumer", return_value=mock)

    return mock


def text():
    from string import ascii_letters

    return _text(alphabet=ascii_letters, min_size=1)


# Override the default text strategy with a customized version
strategies.text = text
