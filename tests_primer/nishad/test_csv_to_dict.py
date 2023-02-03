"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py
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


def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID        , propertyID    , valueNodeType , valueDataType , valueConstraint           , valueConstraintType , minoccurs , maxoccurs , valueShape
    my:IssueShape  , ex:state      ,               ,               , ex:unassigned ex:assigned , picklist            ,           ,           ,
                   , ex:reportedBy ,               ,               ,                           ,                     ,           ,           , my:UserShape
    my:UserShape   , foaf:name     ,               , xsd:string    ,                           ,                     ,           ,           ,
                   , foaf:mbox     , IRI           ,               ,                           ,                     , 1         ,           ,
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
    # with capsys.disabled():
    #     from pprint import pprint
    #     print(Shape)
    #     # pprint(config_dict)
    #     # pprint(csvfile_str)
    #     # pprint(config_dict["prefixes"])
    #     pprint(f'Output: {actual_dict}')
