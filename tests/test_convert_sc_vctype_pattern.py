"""Convert statement constraints of value constraint type "picklist"."""


def _convert_sc_vct_pattern_to_nc(sc):
    """@@@"""
    if sc.get("valueConstraintType") == "pattern":
        nc = {}
        nc["type"] = "NodeConstraint"
        nc["pattern"] = sc.get("valueConstraint")
    return nc


def test_convert_vct_pattern_to_nc():
    """@@@"""
    input_dict = {
        "propertyID": ":nickname",
        "valueConstraint": "John*",
        "valueConstraintType": "pattern",
    }
    output_nc_dict = {"type": "NodeConstraint", "pattern": "John*"}
    assert _convert_sc_vct_pattern_to_nc(input_dict) == output_nc_dict
