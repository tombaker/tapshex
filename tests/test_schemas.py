import io
import json
from pathlib import Path
import pytest
import ruamel.yaml as yaml
from dctap.config import get_config
from dctap.csvreader import csvreader
from tapshex.classes import Shape, StatementTemplate
from tapshex.shexify import shexify
from tapshex.template import SHEX_JINJA

schema_directories = [
        Path("schema1_0_1"),
#       Path("schema1_0_2"),
]

@pytest.mark.parametrize('schemadir', schema_directories)
def test_files_exist(schemadir):
    """Given schema directory has all files needed for tests."""
    assert Path('tapshex.yaml').is_file()
    assert Path(schemadir).joinpath('source.csv').is_file()
    assert Path(schemadir).joinpath('target.tapjson').is_file()
    assert Path(schemadir).joinpath('target.tapjson_expected').is_file()
    assert Path(schemadir).joinpath('from_primer.shexc').is_file()
    assert Path(schemadir).joinpath('from_primer.shexj').is_file()


@pytest.mark.parametrize('schemadir', schema_directories)
def test_from_tapcsv_to_tapjson(schemadir):
    """@@@."""
    config_yamldoc = Path('tapshex.yaml').read_text()
    config_dict = get_config(config_yamldoc=config_yamldoc)
    input_csv = Path(schemadir).joinpath('source.csv').read_text()
    real_output = json.loads(Path(schemadir).joinpath('target.tapjson').read_text())
    expected_output = json.loads(Path(schemadir).joinpath('target.tapjson_expected').read_text())
    tapshapes_dict = csvreader(
        open_csvfile_obj=io.StringIO(input_csv),
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    tapjson_output = json.dumps(tapshapes_dict, sort_keys=True, indent=2)
    # assert real_output == expected_output

def test_shexify_basic():
    """Takes output of dctap, which transforms CSV into Python dict.

    Dctap input is something like:

    shapeID,propertyID,valueNodeType,valueDataType,minoccurs,maxoccurs,mininclusive,maxinclusive
    school:Enrollee,ex:hasGuardian,iri,,1,2
    ,foaf:age,,xsd:integer,,,13,20
    """
    input_dctap_dict = {
        "namespaces": {
            "ex": "http://ex.example/#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "school": "http://school.example/#",
            "foaf": "http://xmlns.com/foaf/0.1/"
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
                    }
                ]
            }
        ]
    }
    shexc_output = shexify(dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA)
    assert 'PREFIX ex: <http://ex.example/#>' in shexc_output
    assert 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>' in shexc_output
    assert 'PREFIX school: <http://school.example/#>' in shexc_output
    assert 'PREFIX foaf: <http://xmlns.com/foaf/0.1/>' in shexc_output
    assert 'school:Enrollee {' in shexc_output
    assert '   ex:hasGuardian IRI {1,2};' in shexc_output
    assert '   foaf:age xsd:integer MaxInclusive 20 MinInclusive 13' in shexc_output
    assert '}' in shexc_output

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
