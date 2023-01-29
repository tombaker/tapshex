"""
Convert from Python dict to ShExC schema string:
- https://shexspec.github.io/primer/#quickStart 
- uses Jinja template at ../../tapshex/template.py
"""

from textwrap import dedent
from tapshex.shexify import shexify
from tapshex.template import SHEX_JINJA


def test_tapjson_to_shexc(capsys):
    """https://shexspec.github.io/primer/#quickStart ."""
    input_dctap_dict = {
        "namespaces": {
            "ex": "http://ex.example/#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "school": "http://school.example/#",
            "foaf": "http://xmlns.com/foaf/0.1/",
        },
        "shapes": [
            {
                "shapeID": "school:Enrollee",
                "statement_templates": [
                    {
                        "propertyID": "ex:hasGuardian",
                        "valueNodeType": "iri",
                        "minoccurs": "1",
                        "maxoccurs": "2",
                    },
                    {
                        "propertyID": "foaf:age",
                        "valueDataType": "xsd:integer",
                        "MinInclusive": "13",
                        "MaxInclusive": "20",
                    },
                ],
            }
        ],
    }
    expected_output = """
    PREFIX ex: <http://ex.example/#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX school: <http://school.example/#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    school:Enrollee {
       ex:hasGuardian IRI;
       foaf:age xsd:integer MaxInclusive 20 MinInclusive 13
    }
    """
    shexc_output = shexify(dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA)
    assert shexc_output == dedent(expected_output)
    with capsys.disabled():
        print(shexc_output)
    # assert "PREFIX ex: <http://ex.example/#>" in shexc_output
    # assert "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>" in shexc_output
    # assert "PREFIX school: <http://school.example/#>" in shexc_output
    # assert "PREFIX foaf: <http://xmlns.com/foaf/0.1/>" in shexc_output
    # assert "school:Enrollee {" in shexc_output
    # assert "   ex:hasGuardian IRI {1,2};" in shexc_output
    # assert "   foaf:age xsd:integer MaxInclusive 20 MinInclusive 13" in shexc_output
    # assert "}" in shexc_output

