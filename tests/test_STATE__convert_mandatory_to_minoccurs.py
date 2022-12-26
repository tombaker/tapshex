"""Convert mandatory to minOccurs."""

import pytest
from tapshex.classes import StatementTemplate

def test_convert_mandatory_to_minoccurs_true():
    """Convert mandatory true to minOccurs 1."""
    st = StatementTemplate()
    st.mandatory = "true"
    st._convert_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minOccurs == 1

def test_convert_mandatory_to_minoccurs_false():
    """Convert mandatory false to minOccurs 0."""
    st = StatementTemplate()
    st.mandatory = "false"
    st._convert_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minOccurs == 0

def test_convert_mandatory_to_minoccurs_empty():
    """If value of mandatory is empty, mandatory is simply deleted."""
    st = StatementTemplate()
    st.mandatory = ""
    st._convert_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minOccurs == ""  # the default value

def test_convert_mandatory_to_minoccurs_neither_true_nor_false():
    """If mandatory is not 'true' or 'false', mandatory is simply is deleted."""
    st = StatementTemplate()
    st.mandatory = "WAHR"
    st._convert_mandatory_to_minoccurs()
    assert not st.mandatory
    assert st.minOccurs == ""  # the default value
