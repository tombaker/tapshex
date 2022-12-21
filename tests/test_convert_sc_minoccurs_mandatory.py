"""Mandatory / repeatable."""

from tapshex.utils import _convert_sc_mandatory_to_sc_min

def test_convert_sc_mandatory_to_sc_min_true():
    """If value of mandatory is "true", then "min" is 1, and mandatory deleted."""
    input_dict = { "mandatory": "true" }
    output_dict = { "min": 1 }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

def test_convert_sc_mandatory_to_sc_min_false():
    """If value of mandatory is "false", then "min" is 0, and mandatory deleted."""
    input_dict = { "mandatory": "false" }
    output_dict = { "min": 0 }
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

def test_convert_sc_mandatory_to_sc_min_empty():
    """If value of mandatory is empty, property is deleted."""
    input_dict = { "mandatory": "" }
    output_dict = {}
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict

def test_convert_sc_mandatory_to_sc_min_neither_true_nor_false():
    """If value of mandatory is not "true" or "false", property is deleted."""
    input_dict = { "mandatory": "WAHR" }
    output_dict = {}
    assert _convert_sc_mandatory_to_sc_min(input_dict) == output_dict
