"""Tests for private functions called by TAPStatementConstraint.validate()."""

import pytest
from dctap2shex.xclasses import TAPStatementConstraintX


def test_valueConstraintType_warn_if_used_without_valueConstraint():
    sc = TAPStatementConstraintX()
    sc.propertyID = ":status"
    sc.valueConstraintType = "pattern"
    sc._valueConstraintType_warn_if_used_without_valueConstraint()
    assert len(sc.sc_warnings) == 1
