from hypothesis import given
from hypothesis import strategies as st

from giap.consumer import Method
from giap.core import GIAP


@given(
    st.one_of(st.integers(min_value=1), st.text()),
    st.text(),
    st.dictionaries(st.text(), st.text()),
    st.one_of(st.none(), st.ip_addresses().map(str)),
    st.text(),
)
def test_track(mock_consumer, id_, name, properties, ip_address, token):
    giap = GIAP(token)

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
    giap = GIAP(token)

    giap.set_profile_properties(id_, properties)

    args = mock_consumer.send.call_args_list[-1][0]
    assert args == (f"/profiles/{id_}", properties, token)

    kwargs = mock_consumer.send.call_args_list[-1][1]
    assert kwargs["method"] is Method.PUT
