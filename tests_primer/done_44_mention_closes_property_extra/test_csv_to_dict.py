"""Convert from CSV string to Python dict using ../../tapshex/template.py."""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "my:":      "http://my.example/#"
    "ex:":      "http://ex.example/#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "rdf:":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
"""

def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID      , extra    , propertyID , valueConstraint
    my:UserShape , rdf:type , rdf:type   , ex:Employee
    my:UserShape , rdf:type , rdf:type   , foaf:Person
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "rdf:": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "extra": "rdf:type",
                "statement_templates": [
                    {
                        "propertyID": "rdf:type",
                        "valueConstraint": "ex:Employee",
                    },
                    {
                        "propertyID": "rdf:type",
                        "valueConstraint": "foaf:Person",
                    },
                ],
            }
        ],
        "warnings": {
            "my:UserShape": {}
        },
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
    assert actual_dict["namespaces"] == expected_dict["namespaces"]
    assert actual_dict == expected_dict

    # with capsys.disabled():
    #     from pprint import pprint
    #     print()
    #     pprint(actual_dict)
