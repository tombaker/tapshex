"""Convert value shape to TripleConstraint."""

def _convert_sc_value_shape_to_tc(sc):
    """@@@"""
    if sc.get("valueShape"):
        tc_predicate = sc.get("propertyID")
        tc = dict()
        tc["type"] = "TripleConstraint"
        tc["predicate"] = tc_predicate
        tc["valueExpr"] = sc.get("valueShape")
    return tc

def test_convert_sc_value_shape_to_tc():
    """@@@
    See: ttp://shex.io/shex-primer/#combined-constraints 

    Whereas Eric seemed to say that a "ShapeAnd" would be 
    required:

            "valueExpr": {
              "type": "ShapeAnd",
              "shapeExprs": [
                {
                  "type": "NodeConstraint",
                  "nodeKind": "iri"
                },
                "http://ex.example/#author"
              ]
            }

    ...maybe to ensure that the value shape is not a BNODE?
    """
    input_dict = {
        "propertyID": "http://purl.org/dc/terms/creator",
    	"valueNodeType": "iri",
        "valueShape": "http://example.org/author",
    }
    output_tc_dict = {
        "type": "TripleConstraint",	
        "predicate": "http://purl.org/dc/terms/creator",
        "valueExpr": "http://example.org/author",
    }
    assert _convert_sc_value_shape_to_tc(input_dict) == output_tc_dict
