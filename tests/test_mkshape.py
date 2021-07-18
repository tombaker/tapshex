"""Convert statement constraints of value constraint type "picklist"."""

def _mkshape(shape_identifier):
    """Makes a shape identifier with shapeID as @id."""
    shape = dict()
    shape["type"] = "Shape"
    shape["id"] = shape_identifier 
    return shape

def test_convert_picklist_of_two_literals():
    """@@@"""
    input_iri = "http://example.org/book" 
    output_dict = {
      "type": "Shape",
      "id": "http://example.org/book" 
    }
    assert _mkshape(input_iri) == output_dict

