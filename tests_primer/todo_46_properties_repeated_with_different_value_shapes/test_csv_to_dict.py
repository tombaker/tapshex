"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.2 Triple Constraints 
  - https://shexspec.github.io/primer/\#tripleConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "ex:":      "http://ex.example/#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "my:":      "http://my.example/#"
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"
"""

# @pytest.mark.skip(reason="WTF?")
def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID            , propertyID      , valueDataType , valueConstraint          , valueConstraintType , valueShape
    my:IssueShape      , ex:state        ,               , ex:accepted ex:resolved  , picklist            ,
                       , ex:reproducedBy ,               ,                          ,                     , my:TesterShape
                       , ex:reproducedBy ,               ,                          ,                     , my:ProgrammerShape
    my:TesterShape     , foaf:name       , xsd:string
                       , ex:role         ,               , ex:testingRole           ,                     ,
    my:ProgrammerShape , foaf:name       , xsd:string
                       , ex:department   ,               , ex:ProgrammingDepartment ,                     ,
    """
    #
    # fmt: on
    expected_dict = {
	    'shapes': [
           {
               'shapeID': 'my:IssueShape',
                'statement_templates': [
                    {
                        'propertyID': 'ex:state',
                        'valueConstraint': ['ex:accepted', 'ex:resolved'],
                        'valueConstraintType': 'picklist'
                    }, {
                        'propertyID': 'ex:reportedBy', 
                        'valueShape': 'my:TesterShape'
                    }, {
                        'propertyID': 'ex:reportedBy', 
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
    # pylint: disable=invalid-name
    actual_dict = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert isinstance(actual_dict, dict)
    assert isinstance(actual_dict["namespaces"], dict)
    assert actual_dict["namespaces"] == expected_dict["namespaces"]
    assert actual_dict == expected_dict

    with capsys.disabled():
        from pprint import pprint
        print()
        pprint(expected_dict)
