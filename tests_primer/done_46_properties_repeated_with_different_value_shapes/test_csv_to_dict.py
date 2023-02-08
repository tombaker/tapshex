"""Convert from CSV string to Python dict using ../../tapshex/template.py."""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "ex:":      "http://ex.example/#"
    "ui:":      "http://ui.example/#"
    "ux:":      "http://ux.example/#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "my:":      "http://my.example/#"
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"
"""

def test_csv_to_dict(capsys):
    """From CSV to Python dict (result_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID            , propertyID      , valueDataType , valueConstraint          , valueConstraintType , valueShape
    my:IssueShape      , ex:state        ,               , ui:accepted ux:resolved  , picklist            ,
                       , ex:reproducedBy ,               ,                          ,                     , my:TesterShape
                       , ex:reproducedBy ,               ,                          ,                     , my:ProgrammerShape
    my:TesterShape     , foaf:name       , xsd:string    ,                          ,                     ,
                       , ex:role         ,               , ex:testingRole           ,                     ,
    my:ProgrammerShape , foaf:name       , xsd:string    ,                          ,                     ,
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
                        'valueConstraint': ['ui:accepted', 'ux:resolved'],
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
            'ex:': 'http://ex.example/#',
            'my:': 'http://my.example/#',
            'ui:': 'http://ui.example/#',
            'ux:': 'http://ux.example/#',
            'foaf:': 'http://xmlns.com/foaf/0.1/',
            'xsd:': 'http://www.w3.org/2001/XMLSchema#',
        },
        'warnings': {
            'my:IssueShape': {}, 
            'my:TesterShape': {},
            'my:ProgrammerShape': {}
        }
    }
    # pylint: disable=invalid-name
    result_dict = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert isinstance(result_dict, dict)
    assert isinstance(result_dict["namespaces"], dict)
    assert result_dict["namespaces"] == expected_dict["namespaces"]
    assert result_dict["warnings"] == expected_dict["warnings"]
    assert result_dict["shapes"][1] == expected_dict["shapes"][1]
    assert result_dict["shapes"][2] == expected_dict["shapes"][2]
    assert result_dict == expected_dict
    # with capsys.disabled():
    #     from pprint import pprint
    #     print()
    #     pprint(result_dict["shapes"][0])
    #     print()
    #     pprint(expected_dict["shapes"][0])
