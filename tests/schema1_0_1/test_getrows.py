"""Read CSV file and return list of rows as Python dictionaries."""

import os
from pathlib import Path
import pytest
from dctap.config import get_config
from tapshex.classes import Shape, StatementTemplate
from dctap.csvreader import _get_rows, _get_tapshapes
from dctap.exceptions import NoDataError, DctapError
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader
from pprint import pprint

@pytest.mark.skip
def test_wtf(capsys):
    """From open CSV file, convert to JSON."""
    HEREDIR = Path(__file__).resolve().parent 
    assert Path(HEREDIR).joinpath("dctap2.csv").exists()
    config_dict = tapshex_config()
    csvfile_str = Path(HEREDIR).joinpath("dctap2.csv").read_text()
    expected_rows_list = [
        {
            "shapeID": "school:Enrollee",
            "propertyID": "ex:hasGuardian"
        }
    ]
    (actual_rows_list, actual_warnings) = _get_rows(
        csvfile_str=csvfile_str, 
        config_dict=config_dict
    )
    assert actual_rows_list == expected_rows_list

def test_get_rows_minimal_warnings(tmp_path, capsys):
    """@@@."""
    config_dict = get_config()
    csvfile_str = 'shapeID,PropertyID\nschool:Enrollee,dc:creator\n'
    expected_rows_list = [
        {
            "shapeID": "school:Enrollee",
            "propertyID": "dc:creator"
        }
    ]
    (actual_rows_list, actual_warnings) = _get_rows(
        csvfile_str=csvfile_str, 
        config_dict=config_dict
    )
    assert actual_rows_list == expected_rows_list
    (tapshapes, tapwarns) = _get_tapshapes(
        rows=actual_rows_list,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    with capsys.disabled():
        print()
        print(tapwarns)


@pytest.mark.skip
def test_csv2json(capsys):
    """From open CSV file, convert to JSON."""
    HEREDIR = Path(__file__).resolve().parent 
    assert Path(HEREDIR).joinpath("dctap.csv").exists()
    config_dict = tapshex_config()
    csvfile_str = Path(HEREDIR).joinpath("dctap.csv").read_text()
    output_jsonobj = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    with capsys.disabled():
        print()
        # pprint(config_dict)
        # pprint(csvfile_str)
        pprint(output_jsonobj)
