"""Mandatory / repeatable."""

from dctap2shex.utils import _convert_sc_repeatable_to_max

def test_convert_sc_repeatable_to_max_true():
    """@@@"""
    input_dict = { "repeatable": "True" }
    output_dict = { "max": -1 }
    assert _convert_sc_repeatable_to_max(input_dict) == output_dict

def test_convert_sc_repeatable_to_max_false():
    """@@@"""
    input_dict = { "repeatable": "False" }
    output_dict = { "max": 1 }
    assert _convert_sc_repeatable_to_max(input_dict) == output_dict

