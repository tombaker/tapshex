"""Test for elements mandatory and repeatable."""

from dctap2shex.xclasses import TAPStatementConstraintX

def test_warn_if_propertyID_not_URI():
    """In ShEx, property ID _must_ be an IRI."""
    sc = TAPStatementConstraintX()
    sc.propertyID = "P31"
    sc._warn_if_propertyID_or_valueDataType_not_IRIlike()
    print(sc.sc_warnings)
    print(dict(sc.sc_warnings))
    print(len(dict(sc.sc_warnings)))
    assert len(dict(sc.sc_warnings)) == 1


def test_warn_if_valueDataType_not_URI():
    """In ShEx, valueShape _must_ be an IRI."""
    sc = TAPStatementConstraintX()
    sc.propertyID = "wdt:P31"
    sc.valueDataType = "date"
    sc._warn_if_propertyID_or_valueDataType_not_IRIlike()
    print(sc.sc_warnings)
    print(dict(sc.sc_warnings))
    print(len(dict(sc.sc_warnings)))
    assert len(dict(sc.sc_warnings)) == 1
