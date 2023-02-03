"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: value shape
  - Asserts that the value is described by another shape.
  - https://shexspec.github.io/primer/#nodeConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA

def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
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
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX my: <http://my.example/#>",
        "my:IssueShape {",
        "ex:reportedBy @my:UserShape",
        "}",
    ]:
        assert line in shexc_output


    # with capsys.disabled():
    #     print()
    #     print()
    #     from tapshex.config import tapshex_config
    #     config_dict = tapshex_config()
    #     print(config_dict["element_aliases"]["mininclusive"])
    #     print("shexc_output:")
    #     for line in shexc_output.splitlines():
    #         print(line)
