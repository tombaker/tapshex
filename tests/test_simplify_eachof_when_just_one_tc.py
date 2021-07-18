"""Convert value shape to TripleConstraint."""

def _simplify_eachof_to_tc_when_just_one(eachof_expression):
    """@@@"""
    if len(eachof_expression.get("expressions")) == 1:
        tc = dict()
        tc["type"] = "TripleConstraint"
        tc["predicate"] = eachof_expression["expressions"][0].get("predicate")
        tc["valueExpr"] = eachof_expression["expressions"][0].get("valueExpr")
        return tc
    else:
        return eachof_expression

def test_simplify_eachof_to_tc_when_just_one():
    """Simplifies "EachOf" object with just one TC to simple TC object."""
    input_dict = {
      "type": "EachOf",
      "expressions": [
        {
          "type": "TripleConstraint",
          "predicate": "http://purl.org/dc/terms/date",
          "valueExpr": {
            "type": "NodeConstraint",
            "datatype": "http://www.w3.org/2001/XMLSchema#date"
          }
        }
      ]
    }
    output_tc_dict = {
      "type": "TripleConstraint",
      "predicate": "http://purl.org/dc/terms/date",
      "valueExpr": {
        "type": "NodeConstraint",
        "datatype": "http://www.w3.org/2001/XMLSchema#date"
      }
    }
    assert _simplify_eachof_to_tc_when_just_one(input_dict) == output_tc_dict

def test_not_simplify_eachof_to_tc_when_more_than_one():
    """Leave "EachOf" object unchanged if it has more than one TC."""
    input_dict = {
      "type": "EachOf",
      "expressions": [
        {
          "type": "TripleConstraint",
          "predicate": "http://purl.org/dc/terms/date",
          "valueExpr": {
            "type": "NodeConstraint",
            "datatype": "http://www.w3.org/2001/XMLSchema#date"
          }
        },
        {
          "type": "TripleConstraint",
          "predicate": "http://ex.example/#status",
          "valueExpr": {
            "type": "NodeConstraint",
            "values": [
              {
                "value": "confidential"
              }
            ]
          }
        }
      ]
    }
    assert _simplify_eachof_to_tc_when_just_one(input_dict) == input_dict
