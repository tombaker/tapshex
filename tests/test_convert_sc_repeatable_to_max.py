"""Mandatory / repeatable."""

from dctap2shex.utils import _convert_sc_repeatable_to_sc_max

def test_convert_sc_repeatable_to_max_true():
    """@@@"""
    input_dict = { "repeatable": "true" }
    output_dict = { "max": -1 }
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict

def test_convert_sc_repeatable_to_max_false():
    """@@@"""
    input_dict = { "repeatable": "false" }
    output_dict = { "max": 1 }
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict

