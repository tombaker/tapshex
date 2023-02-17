"""Convert repeatable to maxoccurs."""

import pytest
from tapshex.config import tapshex_config
from tapshex.classes import StatementTemplate


def test_convert_st_repeatable_to_max_true():
    """If repeatable "true", set maxoccurs to "-1", delete repeatable."""
    st = StatementTemplate()
    st.repeatable = "true"
    assert hasattr(st, 'repeatable')
    assert hasattr(st, 'maxoccurs')
    assert st.repeatable == "true"
    assert st.maxoccurs == ""
    st._convert_st_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxoccurs == "-1"

def test_convert_st_repeatable_to_maxoccurs_when_false():
    """If repeatable "false", set maxoccurs to "1", delete repeatable."""
    st = StatementTemplate()
    st.repeatable = "false"
    assert st.repeatable == "false"
    assert st.maxoccurs == ""
    st._convert_st_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxoccurs == "1"

def test_convert_st_repeatable_to_maxoccurs_when_empty():
    """If repeatable is empty, delete it."""
    st = StatementTemplate()
    st.repeatable = ""
    assert st.repeatable == ""
    st._convert_st_repeatable_to_maxoccurs()
    assert not st.repeatable

def test_convert_st_repeatable_to_maxoccurs_when_neither_true_nor_false():
    """If repeatable is not "true" or "false", delete it."""
    st = StatementTemplate()
    st.repeatable = "WAHR"
    assert st.repeatable == "WAHR"
    st._convert_st_repeatable_to_maxoccurs()
    assert not st.repeatable

def test_convert_st_repeatable_to_maxoccurs_when_true_using_normalize():
    """Same as above using self.normalize()."""
    config_dict = tapshex_config()
    st = StatementTemplate()
    st.repeatable = "true"
    st.normalize(config_dict)
    assert not st.repeatable
    assert st.maxoccurs == "-1"
