"""@@@"""

import pytest
from pprint import pprint
from tapshex.config import tapshex_config
from tapshex.classes import StatementTemplate

def test__dot_placeholder_before_running(capsys):
    """StatementTemplate attributes before running _dot_placeholder()."""
    st = StatementTemplate()
    assert st._dot == True
    triple_constraints = [
        st.minoccurs,
        st.maxoccurs,
        st.mininclusive,
        st.maxinclusive,
        st.minexclusive,
        st.maxexclusive,
        st.minlength,
        st.maxlength,
        st.mandatory,
        st.repeatable,
        st.valueNodeType,
        st.valueDataType,
        st.valueConstraint,
        st.valueConstraintType,
        st.valueShape,
    ]
    for tc in triple_constraints:
        assert tc == ""
        assert not bool(tc)

def test__dot_placeholder_after_added_tripleconstraint(capsys):
    """After adding just one triple constraint, _dot is False."""
    st = StatementTemplate()
    assert st._dot == True
    st.valueNodeType = "IRI"
    st._dot_placeholder()
    assert st._dot == False

def test__dot_placeholder_after_added_tripleconstraint_using_normalize(capsys):
    """@@@"""
    config_dict = tapshex_config()
    st = StatementTemplate()
    assert st._dot == True
    st.valueNodeType = "IRI"
    st.normalize(config_dict)
    assert st._dot == False
