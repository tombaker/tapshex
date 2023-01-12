"""Initializes Python dictionary of type "Shape" with default "EachOf"."""


def _mkshape(shape_identifier):
    """Makes a shape identifier with shapeID as @id."""
    shape = {}
    shape["type"] = "Shape"
    shape["id"] = shape_identifier
    shape["expression"] = {}
    shape["expression"]["type"] = "EachOf"
    shape["expression"]["expressions"] = []
    shape["annotations"] = []
    return shape


def test_convert_picklist_of_two_literals():
    """@@@"""
    input_iri = "http://example.org/book"
    output_dict = {
        "type": "Shape",
        "id": "http://example.org/book",
        "expression": {"type": "EachOf", "expressions": []},
        "annotations": [],
    }
    assert _mkshape(input_iri) == output_dict
