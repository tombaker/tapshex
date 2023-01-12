"""Convert statement constraints of value constraint type "picklist"."""


def _convert_sc_vct_picklist(sc):
    """@@@"""
    if sc.get("valueConstraintType") == "picklist":
        tc_predicate = sc.get("propertyID")
        # breakpoint(context=5)
        valueexpr_values = list()
        for literal_value in sc.get("valueConstraint"):
            nc_value = dict()
            nc_value["value"] = literal_value
            valueexpr_values.append(nc_value)
        tc = dict()
        tc["type"] = "TripleConstraint"
        tc["predicate"] = tc_predicate
        tc["valueExpr"] = dict()
        tc["valueExpr"]["type"] = "NodeConstraint"
        tc["valueExpr"]["values"] = valueexpr_values
    return tc


def test_convert_picklist_of_two_literals():
    """@@@"""
    input_dict = {
        "propertyID": "http://ex.example/#colors",
        "valueConstraint": ["blue", "green"],
        "valueConstraintType": "picklist",
    }
    output_dict = {
        "type": "TripleConstraint",
        "predicate": "http://ex.example/#colors",
        "valueExpr": {
            "type": "NodeConstraint",
            "values": [{"value": "blue"}, {"value": "green"}],
        },
    }
    assert _convert_sc_vct_picklist(input_dict) == output_dict
