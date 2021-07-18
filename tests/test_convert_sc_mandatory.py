"""Mandatory / repeatable."""

def _convert_sc_mandatory_to_sc_min(sc):
    """@@@"""
    if sc.get("mandatory"):
        sc["min"] = 1 
        del sc["mandatory"]
    else:
        sc["min"] = 0
        del sc["mandatory"]
    return sc

def test_convert_sc_mandatory_to_sc_min():
    """@@@"""
    input_dict = {
      "mandatory": "True",
    }
    output_dict = {
      "min": 1,
    }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

