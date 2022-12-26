"""Tests StatementTemplate._are_nonnegative_integers."""

import pytest
from tapshex.classes import StatementTemplate

def test_elements_that_take_nonnegative_integers():
    """Four elements take values that must be nonnegative integers."""
    st = StatementTemplate()
    st.minOccurs = "3"
    st.maxOccurs = "3"
    st.minLength = "3"
    st.maxLength = "3"
    st._are_nonnegative_integers()
    assert len(st.state_warns) == 0

def test_elements_that_take_nonnegative_integers_not():
    """Each of the four elements has a value that is not a nonnegative integer."""
    st = StatementTemplate()
    st.minOccurs = ""  # but empty string should not generate a warning
    st.maxOccurs = "-3"
    st.minLength = "HENCEFORTH"
    st.maxLength = "3.0"
    st._are_nonnegative_integers()
    assert len(st.state_warns) == 3
