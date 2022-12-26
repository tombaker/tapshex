"""Tests StatementTemplate._try_to_coerce_nonnegative_integers."""

import pytest
from tapshex.classes import StatementTemplate

def test_try_to_coerce_nonnegative_integers():
    """Some elements take values that must be nonnegative integers."""
    st = StatementTemplate()
    st.minOccurs = "3"
    st.maxOccurs = "3"
    st.minLength = "3"
    st.maxLength = "3"
    st._try_to_coerce_nonnegative_integers()
    assert len(st.state_warns) == 0

def test_try_to_coerce_nonnegative_integers_not():
    """Four elements have values that are not nonnegative integers."""
    st = StatementTemplate()
    st.minOccurs = ""  # but empty strings should not generate warnings
    st.maxOccurs = "-3"
    st.minLength = "HENCEFORTH"
    st.maxLength = "3.0"
    st._try_to_coerce_nonnegative_integers()
    assert len(st.state_warns) == 3
