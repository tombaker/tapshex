"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints 
  - https://shexspec.github.io/primer/#nodeConstraints

1. Use expected_dict (from test_csv_to_dict.py) as input_dctap_dict.
2. Comment out 'for line in...'.
3. Comment out capsys output.
4. Run pytest 
5. Compare generated ShExC to ./primer.shexc
6. Use generated ShExC to replace lines to 'for lines in...'.
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
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX my: <http://my.example/#>",
        "my:UserShape {",
        "foaf:mbox IRI",
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
