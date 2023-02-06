"""Convert from Python dict to ShExC schema string: using ../../tapshex/template.py."""

# pylint: disable=unused-import,unused-argument,import-error
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA

@pytest.mark.skip(reason="Unclear why dot needed in 'ex:component . {0}'")
def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
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
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX my: <http://my.example/#>",
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "my:IssueShape {",
        "  ex:state [ex:unassigned ex:assigned]",
        "  ex:reportedBy @my:UserShape",
        "}",
        "my:UserShape {",
        "  foaf:name LITERAL {0,1}",
        "  foaf:mbox IRI {0,}",
        "}",
    ]:
        assert line in shexc_output
    
    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
