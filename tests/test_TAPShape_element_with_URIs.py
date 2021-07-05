"""Test for elements mandatory and repeatable."""

from dctap2shex.xclasses import TAPShapeX


def test_warn_if_shapeID_not_URI():
    """In ShEx, ShapeID must be a URI (@@@or blank node?)."""
    shap = TAPShapeX()
    shap.shapeID = "book"
    shap.sc_list = []
    shap.sc_list.append({"propertyID": "dct:creator"})
    shap._warn_if_shapeID_is_not_an_IRI()
    assert len(shap.sh_warnings) == 1
