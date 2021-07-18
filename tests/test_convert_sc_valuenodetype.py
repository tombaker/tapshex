"""Convert statement constraints of value node type "picklist"."""

def _convert_sc_valuenodetype(sc):
    """@@@"""
    if sc.get("valueNodeType"):
        nc = dict()
        nc["type"] = "NodeConstraint"
        nc["nodekind"] = sc.get("valueNodeType")
    return nc

def test_convert_valuenodetype():
    """@@@"""
    input_dict = {
        "propertyID": "http://purl.org/dc/terms/date",
        "valueNodeType": "literal"
    }
    output_dict = {
      "type": "NodeConstraint",
      "nodekind": "literal"
    }
    assert _convert_sc_valuenodetype(input_dict) == output_dict

