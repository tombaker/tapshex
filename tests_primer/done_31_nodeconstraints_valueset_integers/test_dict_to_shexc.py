"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: value set - picklist of strings
  - A node constraint that identifies the datatype of an RDF literal.
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
            "my:": "http://my.example/#",
            "ex:": "http://ex.example/#",
        },
        "shapes": [
            {
                "shapeID": "my:IssueShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:state",
                        "valueConstraint": ["0", "1"],
                        "valueConstraintType": "picklist",
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
        "PREFIX my: <http://my.example/#>",
        "PREFIX ex: <http://ex.example/#>",
        "my:IssueShape", "{",
        "ex:state [0 1]",
        "}",
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     print()
    #     print(shexc_output)
