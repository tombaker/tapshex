"""Convert repeatable to maxOccurs."""

import pytest
from tapshex.classes import StatementTemplate

def test_convert_repeatable_to_maxoccurs_true():
    """Convert repeatable true to maxOccurs -1."""
    st = StatementTemplate()
    st.repeatable = "true"
    st._convert_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxOccurs == -1

def test_convert_repeatable_to_maxoccurs_false():
    """Convert repeatable false to maxOccurs 1."""
    st = StatementTemplate()
    st.repeatable = "false"
    st._convert_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxOccurs == 1

def test_convert_repeatable_to_maxoccurs_empty():
    """If value of repeatable is empty, repeatable is simply deleted."""
    st = StatementTemplate()
    st.repeatable = ""
    st._convert_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxOccurs == ""  # the default value

def test_convert_repeatable_to_maxoccurs_neither_true_nor_false():
    """If value of repeatable is not 'true' or 'false', repeatable is simply deleted."""
    st = StatementTemplate()
    st.repeatable = ""
    st._convert_repeatable_to_maxoccurs()
    assert not st.repeatable
    assert st.maxOccurs == ""  # the default value
