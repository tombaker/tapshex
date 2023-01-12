"""Convert statement constraints of value constraint type "picklist".

Can ignore: 
    "valueNodeType": "IRI"
"""


def _convert_sc_vct_iristem_picklist_to_tc(sc):
    """@@@"""
    if sc.get("valueConstraintType") == "iristem":
        tc_predicate = sc.get("propertyID")
        valueexpr_values = list()
        for iristem in sc.get("valueConstraint"):
            nc_value = dict()
            nc_value["type"] = "IriStem"
            nc_value["stem"] = iristem
            valueexpr_values.append(nc_value)
        tc = dict()
        tc["type"] = "TripleConstraint"
        tc["predicate"] = tc_predicate
        tc["valueExpr"] = dict()
        tc["valueExpr"]["type"] = "NodeConstraint"
        tc["valueExpr"]["values"] = valueexpr_values
    return tc


def test_convert_sc_vct_iristem_picklist_to_nc():
    """@@@"""
    input_dict = {
        "propertyID": "http://purl.org/dc/terms/subject",
        "valueConstraint": [
            "https://id.loc.gov",
            "http://loc.nal.usda.gov",
        ],
        "valueConstraintType": "iristem",
    }
    output_dict = {
        "type": "TripleConstraint",
        "predicate": "http://purl.org/dc/terms/subject",
        "valueExpr": {
            "type": "NodeConstraint",
            "values": [
                {"type": "IriStem", "stem": "https://id.loc.gov"},
                {"type": "IriStem", "stem": "http://loc.nal.usda.gov"},
            ],
        },
    }
    assert _convert_sc_vct_iristem_picklist_to_tc(input_dict) == output_dict
