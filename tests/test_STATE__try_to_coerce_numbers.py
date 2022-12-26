"""Tests StatementTemplate._try_to_coerce_numbers."""

import pytest
from tapshex.classes import StatementTemplate

def test_try_to_coerce_number():
    """Some elements take values that should be coercable to integers or floats."""
    st = StatementTemplate()
    st.minInclusive = "3"
    st.maxInclusive = "-3"
    st.minExclusive = "3.00"
    st.maxExclusive = "3"
    st._try_to_coerce_numbers()
    assert len(st.state_warns) == 0

def test_try_to_coerce_number_nonnumber():
    """Values that are not integers or floats."""
    st = StatementTemplate()
    st.minInclusive = ""  # but empty strings should not generate warnings
    st.maxInclusive = False  # does not generate a warning
    st.minExclusive = "HENCEFORTH"
    st.maxExclusive = r"\d+"
    st._try_to_coerce_numbers()
    assert not "minInclusive" in st.state_warns
    assert not "maxInclusive" in st.state_warns
    assert "minExclusive" in st.state_warns
    assert "maxExclusive" in st.state_warns
    assert len(st.state_warns) == 2
