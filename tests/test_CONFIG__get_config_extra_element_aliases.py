"""Return config dictionary from reading config file."""

import os
import pytest
from pathlib import Path
from tapshex.config import tapshex_config
from tapshex.defaults import DEFAULT_CONFIGFILE
from dctap.exceptions import ConfigError

def test_tapshex_config_file_extra_aliases(tmp_path):
    """
    Get extra element aliases from config file. Note:
    - Dict keys of config_dict["extra_element_aliases"] exactly as in config file.
      - With or without quotes (but quotes necessary if whitespace used).
    - Dict keys of config_dict["element_aliases"] have all been lowercased.
    """
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text("""
    extra_element_aliases:
        ShapID: shapeID
        "Shape Identifier": shapeID
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "ShapID" in config_dict.get("extra_element_aliases")
    assert "Shape Identifier" in config_dict.get("extra_element_aliases")
    assert "shapid" in config_dict.get("element_aliases")
    assert "shapeidentifier" in config_dict.get("element_aliases")

def test_tapshex_config_file_even_propertyid_can_be_aliased(tmp_path):
    """Even propertyID can be aliased."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
        "PropID": "propertyID"
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "propid" in config_dict.get("element_aliases")
    assert config_dict["element_aliases"]["propid"] == "propertyID"

def test_tapshex_config_file_extra_aliases_numbers_acceptable(tmp_path):
    """Numbers as dict keys are handled as strings."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
        1: "shapeID"
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "1" in config_dict.get("element_aliases")

def test_tapshex_config_file_extra_aliases_blank_strings_as_keys_are_acceptable(tmp_path):
    """Blank strings are acceptable as dict keys, even if it makes no sense."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
        "": "shapeID"
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "" in config_dict.get("element_aliases")
    assert config_dict.get("element_aliases")[""] == "shapeID"

def test_get_extra_aliases_dict_none_harmless(tmp_path):
    """Harmless if YAML for extra_element_aliases evaluates to None."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")

def test_get_extra_aliases_list_value(tmp_path):
    """If YAML for extra_element_aliases is a list, converted to empty dict."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
    - one
    - two
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")

def test_get_extra_aliases_dict_handles_spaces_and_punctuation(tmp_path):
    """In addition to lowercasing, drops punctuation and spaces."""
    os.chdir(tmp_path)
    Path(DEFAULT_CONFIGFILE).write_text(
        """
    extra_element_aliases:
        "S  h,apid": "shapeID"
        "   f  oo,BAR": "shapeID"
    """
    )
    config_dict = tapshex_config()
    assert "extra_element_aliases" in config_dict
    assert "propertyid" in config_dict.get("element_aliases")
    assert "shapid" in config_dict.get("element_aliases")
    assert "foobar" in config_dict.get("element_aliases")
