"""Tests for tapshex.csvreader."""

import os
from pathlib import Path
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader
from pprint import pprint

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "ex:":      "http://ex.example/#"
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "school:":  "http://school.example/#"
"""

def test_csv2json(capsys):
    """From open CSV file, convert to JSON."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    tap_csv = """\
    # https://shexspec.github.io/primer/#quickStart
    shapeID         , propertyID     , valueNodeType , valueDataType , minoccurs , maxoccurs , mininclusive , maxinclusive
    school:Enrollee , ex:hasGuardian , iri           ,               , 1         , 2
                    , foaf:age       ,               , xsd:integer   ,           ,           , 13           , 20
    """
    expected_output_pyobj = {
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
    #
    HEREDIR = Path(__file__).resolve().parent
    csvfile_str = Path(HEREDIR).joinpath("dctap.csv").read_text()
    output_pyobj_from_disk = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    #
    csvfile_str = tap_csv
    output_pyobj_from_variable = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert isinstance(output_pyobj_from_disk, dict)
    assert isinstance(output_pyobj_from_variable, dict)
    assert isinstance(output_pyobj_from_disk["namespaces"], dict)
    assert isinstance(output_pyobj_from_variable["namespaces"], dict)
    assert output_pyobj_from_disk["namespaces"] == expected_output_pyobj["namespaces"]
    assert output_pyobj_from_variable["namespaces"] == expected_output_pyobj["namespaces"]
    assert isinstance(output_pyobj_from_disk["shapes"], list)
    assert sorted(output_pyobj_from_variable["shapes"]) == sorted(expected_output_pyobj["shapes"])
    assert output_pyobj_from_disk == expected_output_pyobj
    assert output_pyobj_from_variable == expected_output_pyobj
    # with capsys.disabled():
    #     print()
    #     # pprint(config_dict)
    #     # pprint(csvfile_str)
    #     # pprint(config_dict["prefixes"])
    #     pprint(f'output_pyobj_from_variable["namespaces"]: {output_pyobj_from_variable["namespaces"]}')
    #     pprint(f'expected_output_pyobj["namespaces"]: {expected_output_pyobj["namespaces"]}')
