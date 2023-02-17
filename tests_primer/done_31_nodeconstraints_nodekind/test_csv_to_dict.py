"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: node kind
  - A node constraint that specifies whether an RDF data node is of 
    lind Literal, IRI, BNode, or NonLiteral
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
    "foaf:":    "http://xmlns.com/foaf/0.1/"
"""


def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID      , propertyID , valueNodeType
    my:UserShape , foaf:mbox  , IRI
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "foaf:mbox",
                        "valueNodeType": "iri",
                    },
                ],
            }
        ],
        "warnings": {"my:UserShape": {}},
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
    assert sorted(actual_dict["shapes"]) == sorted(expected_dict["shapes"])
    assert actual_dict == expected_dict
    # with capsys.disabled():
    #     from pprint import pprint
    #     print(Shape)
    #     # pprint(config_dict)
    #     # pprint(csvfile_str)
    #     # pprint(config_dict["prefixes"])
    #     pprint(f'Output: {actual_dict}')
