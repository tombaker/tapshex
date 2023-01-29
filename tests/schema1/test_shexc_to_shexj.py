"""
Convert from Python dict to ShExC schema string:
- https://shexspec.github.io/primer/#quickStart 
- uses Jinja template at ../../tapshex/template.py
"""

from textwrap import dedent
import pytest
from tapshex.shexify import shexc_to_shexj

@pytest.mark.skip(reason="postponed")
def test_shexc_to_shexj(capsys):
    """Convert ShExC schema into ShExJ schema."""
    input_shexc = """
    PREFIX ex: <http://ex.example/#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX school: <http://school.example/#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    school:Enrollee {
       ex:hasGuardian IRI;
       foaf:age xsd:integer MaxInclusive 20 MinInclusive 13
    }
    """
    expected_output_shexj = {
        "@context": "http://www.w3.org/ns/shex.jsonld",
        "type": "Schema",
        "shapes": [
            {
                "id": "http://school.example/#enrolleeAge",
                "type": "NodeConstraint",
                "datatype": "http://www.w3.org/2001/XMLSchema#integer",
                "mininclusive": 13,
                "maxinclusive": 20
            },
            {
                "id": "http://school.example/#Enrollee",
                "type": "Shape",
                "expression": {
                    "type": "TripleConstraint",
                    "min": 1,
                    "max": 2,
                    "predicate": "http://ex.example/#hasGuardian",
                    "valueExpr": {
                        "type": "NodeConstraint",
                        "nodeKind": "iri"
                    }
                }
            }
        ]
    }
    output_shexj = shexc_to_shexj(shexc_schema=input_shexc)
    # assert output_shexj == expected_output_shexj
    with capsys.disabled():
        from pprint import pprint
        print()
        output_shexj
        # pprint(f"output_shexj: {output_shexj}")
        # print(f"expected_output_shexj: {type(expected_output_shexj)}")
        # print(f"output_shexj: {type(output_shexj)}")

