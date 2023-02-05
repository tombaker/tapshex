"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: literal datatype
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
            "rdf:": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "rdf:type",
                        "valueConstraint": "foaf:Person",
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
        'PREFIX my: <http://my.example/#>',
        'my:UserShape {',
        'rdf:type [foaf:Person]',
        '}',
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
