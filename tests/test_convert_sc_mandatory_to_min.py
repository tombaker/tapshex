"""Mandatory / repeatable."""

from dctap2shex.utils import _convert_sc_mandatory_to_sc_min

def test_convert_sc_mandatory_to_sc_min_true():
    """@@@"""
    input_dict = {
      "mandatory": "true",
    }
    output_dict = {
      "min": 1,
    }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

def test_convert_sc_mandatory_to_sc_min_false():
    """@@@"""
    input_dict = {
      "mandatory": "false",
    }
    output_dict = {
      "min": 0,
    }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

