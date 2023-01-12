"""Convert statement constraints of value constraint type "picklist"."""


def _convert_sc_valuedatatype(sc):
    """@@@"""
    if sc.get("valueDataType"):
        tc_predicate = sc.get("propertyID")
        tc = {}
        tc["type"] = "TripleConstraint"
        tc["predicate"] = tc_predicate
        tc["valueExpr"] = {}
        tc["valueExpr"]["type"] = "NodeConstraint"
        tc["valueExpr"]["datatype"] = sc.get("valueDataType")
    return tc


def test_convert_picklist_of_two_literals():
    """@@@"""
    input_dict = {
        "propertyID": "http://purl.org/dc/terms/date",
        "valueDataType": "http://www.w3.org/2001/XMLSchema#date",
    }
    output_dict = {
        "type": "TripleConstraint",
        "predicate": "http://purl.org/dc/terms/date",
        "valueExpr": {
            "type": "NodeConstraint",
            "datatype": "http://www.w3.org/2001/XMLSchema#date",
        },
    }
    assert _convert_sc_valuedatatype(input_dict) == output_dict
