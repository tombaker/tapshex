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
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
"""

def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID            , closed , propertyID , valueNodeType , valueDataType
    my:OpenUserShape   ,        , foaf:name  ,               , xsd:string
                       ,        , foaf:mbox  , IRI           ,
    my:ClosedUserShape , True   , foaf:name  ,               , xsd:string
                       ,        , foaf:mbox  , IRI           ,
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
            "xsd:": "http://www.w3.org/2001/XMLSchema#",
        },
        "shapes": [
            {
                "shapeID": "my:OpenUserShape",
                "statement_templates": [
                    {
                        "propertyID": "foaf:name",
                        "valueDataType": "xsd:string",
                    },
                    {
                        "propertyID": "foaf:mbox",
                        "valueNodeType": "iri",
                    },
                ],
            },
            {
                "shapeID": "my:ClosedUserShape",
                "closed": "True",
                "statement_templates": [
                    {
                        "propertyID": "foaf:name",
                        "valueDataType": "xsd:string",
                    },
                    {
                        "propertyID": "foaf:mbox",
                        "valueNodeType": "iri",
                    },
                ],
            }
        ],
        "warnings": {"my:OpenUserShape": {}, "my:ClosedUserShape": {}},
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
    #     from pprint import pprint
    #     print()
    #     pprint(expected_dict)
    #     print()
    #     print()
    #     print()
    #     pprint(actual_dict)
