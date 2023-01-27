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
    HEREDIR = Path(__file__).resolve().parent
    assert Path(HEREDIR).joinpath("dctap.csv").exists()
    csvfile_str = Path(HEREDIR).joinpath("dctap.csv").read_text()
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    output_pyobj = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
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
    # output_pyobj, the output of tapshex_csvreader:
    # output_pyobj: dict
    assert isinstance(output_pyobj, dict)
    #
    # output_pyobj["namespaces"]: dict
    assert isinstance(output_pyobj["namespaces"], dict)
    assert output_pyobj["namespaces"] == expected_output_pyobj["namespaces"]
    #
    # output_pyobj["shapes"]: list
    assert isinstance(output_pyobj["shapes"], list)
    assert sorted(output_pyobj["shapes"]) == sorted(expected_output_pyobj["shapes"])
    #
    with capsys.disabled():
        print()
        # pprint(config_dict)
        # pprint(csvfile_str)
        # pprint(config_dict["prefixes"])
        pprint(f'output_pyobj["namespaces"]: {output_pyobj["namespaces"]}')
        pprint(f'expected_output_pyobj["namespaces"]: {expected_output_pyobj["namespaces"]}')
