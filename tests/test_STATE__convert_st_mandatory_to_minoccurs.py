"""Convert mandatory to minoccurs."""

import pytest
from tapshex.config import tapshex_config
from tapshex.classes import StatementTemplate


def test_convert_st_mandatory_to_max_true():
    """If mandatory "true", set minoccurs to "-1", delete mandatory."""
    st = StatementTemplate()
    st.mandatory = "true"
    assert hasattr(st, 'mandatory')
    assert hasattr(st, 'minoccurs')
    assert st.mandatory == "true"
    assert st.minoccurs == ""
    st._convert_st_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minoccurs == "1"

def test_convert_st_mandatory_to_minoccurs_when_false():
    """If mandatory "false", set minoccurs to "1", delete mandatory."""
    st = StatementTemplate()
    st.mandatory = "false"
    assert st.mandatory == "false"
    assert st.minoccurs == ""
    st._convert_st_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minoccurs == "0"

def test_convert_st_mandatory_to_minoccurs_when_empty():
    """If mandatory is empty, delete it."""
    st = StatementTemplate()
    st.mandatory = ""
    assert st.mandatory == ""
    st._convert_st_mandatory_to_minoccurs()
    assert not st.mandatory

def test_convert_st_mandatory_to_minoccurs_when_neither_true_nor_false():
    """If mandatory is not "true" or "false", delete it."""
    st = StatementTemplate()
    st.mandatory = "WAHR"
    assert st.mandatory == "WAHR"
    st._convert_st_mandatory_to_minoccurs()
    assert not st.mandatory

def test_convert_st_mandatory_to_minoccurs_when_true_using_normalize():
    """Same as above using self.normalize()."""
    config_dict = tapshex_config()
    st = StatementTemplate()
    st.mandatory = "true"
    st.normalize(config_dict)
    assert not st.mandatory
    assert st.minoccurs == "1"
