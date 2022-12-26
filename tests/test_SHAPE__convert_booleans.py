"""For Boolean elements in Shape, convert 'true' and 'false' to 1 and 0."""

import pytest
from tapshex.classes import Shape

def test_convert_booleans_true():
    """Convert propertyExtra true to 1."""
    st = Shape()
    st.closed = "true"
    st.start = "true"
    st._convert_booleans()
    assert st.closed == 1
    assert st.start == 1

def test_convert_booleans_false():
    """Convert propertyExtra false to 0."""
    st = Shape()
    st.closed = "false"
    st.start = "false"
    st._convert_booleans()
    assert st.closed == 0
    assert st.start == 0

def test_convert_booleans_empty():
    """If value of propertyExtra is empty, propertyExtra is simply deleted."""
    st = Shape()
    st.closed = ""
    st.start= ""
    st._convert_booleans()
    assert st.closed == ""  # the default value
    assert st.start == ""  # the default value

def test_convert_booleans_neither_true_nor_false():
    """If propertyExtra is not 'true' or 'false', propertyExtra is simply is deleted."""
    st = Shape()
    st.closed = "WAHR"
    st.start= "WAHR"
    st._convert_booleans()
    assert st.closed == "WAHR"  # left unchanged
    assert st.start == "WAHR"  # left unchanged
