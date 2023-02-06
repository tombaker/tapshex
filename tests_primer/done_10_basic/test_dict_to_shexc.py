"""
Convert from Python dict to ShExC schema string:
- https://shexspec.github.io/primer/#quickStart 
- uses Jinja template at ../../tapshex/template.py
"""

from textwrap import dedent
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA

def test_tapdict_to_shexc(capsys):
    """https://shexspec.github.io/primer/#quickStart ."""
    input_dctap_dict = {
        "namespaces": {
            "ex:": "http://ex.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
            "xsd:": "http://www.w3.org/2001/XMLSchema#",
            "school:": "http://school.example/#",
        },
        "shapes": [
            {
                "shapeID": "school:Enrollee",
                "statement_templates": [
                    {
                        "maxoccurs": "2",
                        "minoccurs": "1",
                        "propertyID": "ex:hasGuardian",
                        "valueNodeType": "iri",
                    },
                    {
                        "maxinclusive": "20",
                        "mininclusive": "13",
                        "propertyID": "foaf:age",
                        "valueDataType": "xsd:integer",
                    },
                ],
            }
        ],
        "warnings": {"school:Enrollee": {}},
    }
    shexc_output = tapdict_to_shexc(dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA)
    for line in [
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX school: <http://school.example/#>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "school:Enrollee", "{",
        "  ex:hasGuardian IRI {1,2}",
        "  foaf:age xsd:integer MinInclusive 13 MaxInclusive 20",
        "}",
    ]:
        assert line in shexc_output
    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)

