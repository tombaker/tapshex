"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py
- 3.1 Node Constraints: literal datatype
  - A node constraint that identifies the datatype of an RDF literal.
  - https://shexspec.github.io/primer/#nodeConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import dctap_csvreader

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
    shapeID      , propertyID , valueConstraint
    my:UserShape , rdf:type   , ex:Employee
    my:UserShape , rdf:type   , foaf:Person
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "ex:": "http://ex.example/#",
            "rdf:": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "foaf:": "http://xmlns.com/foaf/0.1/"
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
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
    actual_dict = dctap_csvreader(
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
    #     print("But... ", end="")
        # from pprint import pprint
        # print()
        # pprint(expected_dict["namespaces"])
        # print()
        # pprint(actual_dict["namespaces"])
