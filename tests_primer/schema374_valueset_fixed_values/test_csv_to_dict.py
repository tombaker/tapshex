"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: literal datatype
  - Node constraint that identifies datatype of RDF literal.
  - https://shexspec.github.io/primer/#nodeConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "rdf:":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "my:":      "http://my.example/#"
"""

def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID       , propertyID , valueConstraint
    my:UserShape  , rdf:type   , foaf:Person
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "rdf:": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "rdf:type",
                        "valueConstraint": "foaf:Person",
                    },
                ],
            }
        ],
        "warnings": {"my:UserShape": {}},
    }
    # pylint: disable=invalid-name
    actual_dict = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert isinstance(actual_dict, dict)
    assert isinstance(actual_dict["namespaces"], dict)
    # Note: "foaf:" not listed: prefixes in used in valueConstraint not recognized
    assert "foaf:" in config_dict["prefixes"]
    assert "foaf:" not in actual_dict["namespaces"]
    assert actual_dict["namespaces"] == expected_dict["namespaces"]
    assert actual_dict == expected_dict
    # with capsys.disabled():
    #     from pprint import pprint
    #     print()
    #     pprint(config_dict["prefixes"])
    #     pprint(expected_dict["namespaces"])
    #     print()
    #     pprint(actual_dict["namespaces"])
