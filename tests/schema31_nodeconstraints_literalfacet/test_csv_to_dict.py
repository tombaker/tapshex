"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py
- 3.1 Node Constraints: literal facet
  - A node constraint that applies XML Schema constraining facets.
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
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"
"""


def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID      , propertyID  , valueDataType , mininclusive , maxinclusive
    my:UserShape , ex:shoeSize , xsd:float     , 5.5          , 12.5
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "ex:": "http://ex.example/#",
            "my:": "http://my.example/#",
            "xsd:": "http://www.w3.org/2001/XMLSchema#",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:shoeSize",
                        "valueDataType": "xsd:float",
                        "mininclusive": "5.5",
                        "maxinclusive": "12.5",
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
