"""Convert from Python dict to ShExC schema string using ../../tapshex/template.py."""

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
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX my: <http://my.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:OpenUserShape  {",
        "my:ClosedUserShape CLOSED {",
        "  foaf:name xsd:string",
        "  foaf:mbox IRI",
        "}",
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
