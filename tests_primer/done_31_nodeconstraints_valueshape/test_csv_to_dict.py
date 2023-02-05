"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: value shape
  - Asserts that the value is described by another shape.
  - https://shexspec.github.io/primer/#nodeConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "ex:":      "http://ex.example/#"
    "my:":      "http://my.example/#"
"""


def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID       , propertyID    , valueShape
    my:IssueShape , ex:reportedBy , my:UserShape
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "ex:": "http://ex.example/#",
            "my:": "http://my.example/#",
        },
        "shapes": [
            {
                "shapeID": "my:IssueShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:reportedBy",
                        "valueShape": "my:UserShape",
                    },
                ],
            }
        ],
        "warnings": {"my:IssueShape": {}},
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
    assert sorted(actual_dict["shapes"]) == sorted(expected_dict["shapes"])
    assert actual_dict == expected_dict

    # with capsys.disabled():
    #     from pprint import pprint
    #     print(Shape)
    #     # pprint(config_dict)
    #     # pprint(csvfile_str)
    #     # pprint(config_dict["prefixes"])
    #     pprint(f'Output: {actual_dict}')
