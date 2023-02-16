"""@@@"""

import pytest
from pprint import pprint
from tapshex.classes import StatementTemplate

def test__dot_placeholder(capsys):
    """@@@"""
    st = StatementTemplate()
    assert st.dot_placeholder == True
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
    st.valueNodeType = "IRI"
    st._dot_placeholder()
    assert st.dot_placeholder == False
    # with capsys.disabled():
    #     print()
    #     pprint(st.dot_placeholder)
