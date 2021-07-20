"""Convert repeatable to max."""

from dctap2shex.utils import _convert_sc_repeatable_to_sc_max

def test_convert_sc_repeatable_to_max_true():
    """If value of repeatable is "true", then "min" is 1, and repeatable deleted."""
    input_dict = { "repeatable": "true" }
    output_dict = { "max": -1 }
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict

def test_convert_sc_repeatable_to_max_false():
    """If value of repeatable is "false", then "min" is 0, and repeatable deleted."""
    input_dict = { "repeatable": "false" }
    output_dict = { "max": 1 }
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict

def test_convert_sc_repeatable_to_sc_max_empty():
    """If value of repeatable is empty, property is deleted."""
    input_dict = { "repeatable": "" }
    output_dict = {}
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict

def test_convert_sc_repeatable_to_sc_max_neither_true_nor_false():
    """If value of repeatable is not "true" or "false", property is deleted."""
    input_dict = { "repeatable": "WAHR" }
    output_dict = {}
    assert _convert_sc_repeatable_to_sc_max(input_dict) == output_dict
