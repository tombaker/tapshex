"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py
"""

# pylint: disable=unused-import,unused-argument,import-error
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA


@pytest.mark.skip(reason="Template needs to support CLOSED")
def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
            "xsd:": "http://www.w3.org/2001/XMLSchema#",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "foaf:name",
                        "valueDataType": "xsd:string",
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
        "PREFIX my: <http://my.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:UserShape {",
        "  foaf:name xsd:string",
        "}",
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
