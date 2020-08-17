from hypothesis import given
from hypothesis import strategies as st

from giap.consumer import Method, Operation
from giap.core import GIAP


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.text(),
    st.dictionaries(st.text(), st.text()),
    st.one_of(st.none(), st.ip_addresses().map(str)),
    st.text(),
)
def test_track(mock_consumer, id_, name, properties, ip_address, token):
    giap = GIAP(token, "")

    giap.track(id_, name, properties, ip_address)

    args = mock_consumer.send.call_args_list[-1][0]
    assert args[0] == "/events"
    assert args[2] == token

    data = args[1]["events"][0]
    assert data["$distinct_id"] == str(id_)
    assert data["$name"] == name
    assert isinstance(data["$time"], int)
    assert "$lib" in data
    assert "$lib_version" in data

    if ip_address is not None:
        assert data["$sender_ip"] == ip_address

    assert set(properties.items()).issubset(data.items())


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.dictionaries(st.text(), st.text()),
    st.text(),
)
def test_set_profile_properties(mock_consumer, id_, properties, token):
    giap = GIAP(token, "")

    giap.set_profile_properties(id_, properties)

    args = mock_consumer.send.call_args_list[-1][0]
    assert args == ("/profiles/{}".format(id_), properties, token)

    kwargs = mock_consumer.send.call_args_list[-1][1]
    assert kwargs["method"] is Method.PUT


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.text(),
    st.one_of(st.integers(), st.floats()),
    st.text(),
)
def test_increase(mock_consumer, id_, property_name, value, token):
    giap = GIAP(token, "")

    giap.increase(id_, property_name, value)

    args = mock_consumer.send.call_args_list[-1][0]
    data = {"operation": Operation.INCREASE, "value": value}
    assert args == ("/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name), data, token)

    kwargs = mock_consumer.send.call_args_list[-1][1]
    assert kwargs["method"] is Method.PUT


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.text(),
    st.lists(st.one_of(st.integers(), st.floats(), st.text())),
    st.text(),
)
def test_append(mock_consumer, id_, property_name, value, token):
    giap = GIAP(token, "")

    giap.append(id_, property_name, value)

    args = mock_consumer.send.call_args_list[-1][0]
    data = {"operation": Operation.APPEND, "value": value}
    assert args == ("/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name), data, token)

    kwargs = mock_consumer.send.call_args_list[-1][1]
    assert kwargs["method"] is Method.PUT


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.text(),
    st.lists(st.one_of(st.integers(), st.floats(), st.text())),
    st.text(),
)
def test_remove(mock_consumer, id_, property_name, value, token):
    giap = GIAP(token, "")

    giap.remove(id_, property_name, value)

    args = mock_consumer.send.call_args_list[-1][0]
    data = {"operation": Operation.REMOVE, "value": value}
    assert args == ("/profiles/{id_}/{property_name}".format(id_=id_, property_name=property_name), data, token)

    kwargs = mock_consumer.send.call_args_list[-1][1]
    assert kwargs["method"] is Method.PUT
