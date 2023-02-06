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
"""

def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID       , propertyID    , valueNodeType , valueConstraint           , valueConstraintType , valueShape   , minoccurs , maxoccurs
    my:IssueShape , ex:state      ,               , ex:unassigned ex:assigned , picklist            ,              ,
                  , ex:reportedBy ,               ,                           ,                     , my:UserShape ,           ,
    my:UserShape  , foaf:name     , literal       ,                           ,                     ,              , 0         , 1
                  , foaf:mbox     , iri           ,                           ,                     ,              , 0         ,
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "ex:": "http://ex.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
        },
        "shapes": [
            {
                "shapeID": "my:IssueShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:state",
                        "valueConstraint": ["ex:unassigned", "ex:assigned"],
                        "valueConstraintType": "picklist",
                    },
                    {
                        "propertyID": "ex:reportedBy",
                        "valueShape": "my:UserShape",
                    },
                ],
            },
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "foaf:name",
                        "valueNodeType": "literal",
                        "minoccurs": "0",
                        "maxoccurs": "1",
                    },
                    {
                        "propertyID": "foaf:mbox",
                        "valueNodeType": "iri",
                        "minoccurs": "0",
                    },
                ],
            }
        ],
        "warnings": {
            "my:UserShape": {},
            "my:IssueShape": {}
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
    #     # pprint(config_dict)
    #     # pprint(csvfile_str)
    #     # pprint(config_dict["prefixes"])
    #     print()
    #     pprint(expected_dict)
    #     print()
    #     pprint(actual_dict)
