"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints 
  - https://shexspec.github.io/primer/#nodeConstraints
  - Numeric facets, which apply only to numeric RDF literals
    MinInclusive, MinExclusive, MaxInclusive, MaxExclusive, TotalDigits, FractionDigits
  - String facets, which apply to all RDF literals
    Length, MinLength, MaxLength, Pattern
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
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX my: <http://my.example/#>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:UserShape {",
        "ex:shoeSize xsd:float MinInclusive 5.5 MaxInclusive 12.5",
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
