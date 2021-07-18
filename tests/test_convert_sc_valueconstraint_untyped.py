"""Convert untyped value constraint."""

def _convert_sc_vc_untyped_to_nc(sc):
    """@@@"""
    values_value = dict()
    values_value["value"] = sc.get("valueConstraint")
    if sc.get("valueConstraint"):
        if not sc.get("valueConstraintType"):
            nc = dict()
            nc["type"] = "NodeConstraint"
            nc["values"] = list()
            nc["values"].append(values_value)
    return nc

def test_convert_picklist_of_two_literals():
    """@@@"""
    input_dict = {
      "propertyID": ":status",
      "valueConstraint": "confidential"
    }
    output_tc_dict = {
      "type": "NodeConstraint",
      "values": [
        {
          "value": "confidential"
        }
      ]
    }
    assert _convert_sc_vc_untyped_to_nc(input_dict) == output_tc_dict
