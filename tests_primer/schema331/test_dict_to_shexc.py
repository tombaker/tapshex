"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.3 Grouping Triple Constaints in Shapes
  - https://shexspec.github.io/primer/#simple-expressions
"""

# pylint: disable=unused-import,unused-argument,import-error
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA

@pytest.mark.skip(reason="Unclear how to indicate n in {m,n}")
def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
	    'shapes': [
           {
               'shapeID': 'my:IssueShape',
                'statement_templates': [
                    {
                        'propertyID': 'ex:state',
                        'valueConstraint': ['ex:unassigned', 'ex:assigned'],
                        'valueConstraintType': 'picklist'
                    }, {
                        'propertyID': 'ex:reportedBy', 
                        'valueShape': 'my:UserShape'
                    }
                ]
            }, {
                'shapeID': 'my:UserShape',
                'statement_templates': [
                    {
                        'propertyID': 'foaf:name', 
                        'valueDataType': 'xsd:string'
                    }, {
                        'propertyID': 'foaf:mbox', 
                        'valueNodeType': 'iri', 
                        'minoccurs': '1'
                    }
                ]
            }
        ],
        'namespaces': {
            'xsd:': 'http://www.w3.org/2001/XMLSchema#',
            'ex:': 'http://ex.example/#',
            'foaf:': 'http://xmlns.com/foaf/0.1/',
            'my:': 'http://my.example/#'
        },
        'warnings': {
            'my:IssueShape': {}, 
            'my:UserShape': {}
        }
    }
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX my: <http://my.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:IssueShape {",
        "ex:state [ex:unassigned ex:assigned]",
        "ex:reportedBy @my:UserShape",
        "}",
        "my:UserShape {",
        "  foaf:name xsd:string",
        "foaf:mbox IRI {1,}",
        "}",
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
