"""Mandatory / repeatable."""

def _convert_sc_mandatory_to_sc_min(sc):
    """@@@"""
    if sc.get("mandatory").lower() == "true":
        sc["min"] = 1 
        del sc["mandatory"]
    else:
        sc["min"] = 0
        del sc["mandatory"]
    return sc

def test_convert_sc_mandatory_to_sc_min_true():
    """@@@"""
    input_dict = {
      "mandatory": "True",
    }
    output_dict = {
      "min": 1,
    }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

def test_convert_sc_mandatory_to_sc_min_false():
    """@@@"""
    input_dict = {
      "mandatory": "False",
    }
    output_dict = {
      "min": 0,
    }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

