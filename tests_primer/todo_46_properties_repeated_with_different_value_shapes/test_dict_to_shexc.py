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

def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
	    'shapes': [
           {
               'shapeID': 'my:IssueShape',
                'statement_templates': [
                    {
                        'propertyID': 'ex:state',
                        'valueConstraint': ['ex:accepted', 'ex:resolved'],
                        'valueConstraintType': 'picklist'
                    }, {
                        'propertyID': 'ex:reproducedBy', 
                        'valueShape': 'my:TesterShape'
                    }, {
                        'propertyID': 'ex:reproducedBy', 
                        'valueShape': 'my:ProgrammerShape'
                    }
                ]
            }, {
                'shapeID': 'my:TesterShape',
                'statement_templates': [
                    {
                        'propertyID': 'foaf:name', 
                        'valueDataType': 'xsd:string'
                    }, {
                        'propertyID': 'ex:role', 
                        'valueConstraint': 'ex:testingRole', 
                    }
                ]
            }, {
                'shapeID': 'my:ProgrammerShape',
                'statement_templates': [
                    {
                        'propertyID': 'foaf:name', 
                        'valueDataType': 'xsd:string'
                    }, {
                        'propertyID': 'ex:department', 
                        'valueConstraint': 'ex:ProgrammingDepartment', 
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
            'my:TesterShape': {},
            'my:ProgrammerShape': {}
        }
    }
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX ex: <http://ex.example/#>",
        "PREFIX my: <http://my.example/#>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:IssueShape", "{",
        "ex:state [ex:accepted ex:resolved]",
        "ex:reproducedBy @my:TesterShape",
        "ex:reproducedBy @my:ProgrammerShape",
        "}",
        "my:TesterShape", "{",
        "  foaf:name xsd:string",
        "  ex:role [ex:testingRole]",
        "  ex:department [ex:ProgrammingDepartment]",
        "}",
        "my:ProgrammerShape", "{",
    ]:
        assert line in shexc_output

    # with capsys.disabled():
    #     print()
    #     print()
    #     for line in shexc_output.splitlines():
    #         print(line)
