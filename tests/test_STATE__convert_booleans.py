"""For Boolean elements in StatementTemplate, convert 'true' and 'false' to 1 and 0."""

import pytest
from tapshex.classes import StatementTemplate

def test_convert_booleans_true():
    """Convert propertyExtra true to 1."""
    st = StatementTemplate()
    st.propertyExtra = "true"
    st._convert_booleans()
    assert st.propertyExtra == 1

def test_convert_booleans_false():
    """Convert propertyExtra false to 0."""
    st = StatementTemplate()
    st.propertyExtra = "false"
    st._convert_booleans()
    assert st.propertyExtra == 0

def test_convert_booleans_empty():
    """If value of propertyExtra is empty, propertyExtra is simply deleted."""
    st = StatementTemplate()
    st.propertyExtra = ""
    st._convert_booleans()
    assert st.propertyExtra == ""  # the default value

def test_convert_booleans_neither_true_nor_false():
    """If propertyExtra is not 'true' or 'false', propertyExtra is simply is deleted."""
    st = StatementTemplate()
    st.propertyExtra = "WAHR"
    st._convert_booleans()
    assert st.propertyExtra == "WAHR"  # left unchanged
