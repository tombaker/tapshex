"""Convert statement constraints of value constraint type "picklist"."""

def _convert_sc_vct_languagetag_picklist(sc):
    """@@@"""
    if sc.get("valueConstraintType") == "languagetag":
        tc_predicate = sc.get("propertyID")
        # breakpoint(context=5)
        valueexpr_values = list()
        for langtag in sc.get("valueConstraint"):
            nc_value = dict()
            nc_value["type"] = "Language"
            nc_value["languageTag"] = langtag
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
      "propertyID": "http://ex.example/#description",
      "valueConstraint": [
          "fr",
          "it",
          "en"
      ],
      "valueConstraintType": "languagetag"
    }
    output_dict = {
      "type": "TripleConstraint",
      "predicate": "http://ex.example/#description",
      "valueExpr": {
        "type": "NodeConstraint",
        "values": [
          {
            "type": "Language",
            "languageTag": "fr"
          },
          {
            "type": "Language",
            "languageTag": "it"
          },
          {
            "type": "Language",
            "languageTag": "en"
          }
        ]
      }
    }
    assert _convert_sc_vct_languagetag_picklist(input_dict) == output_dict

