"""Tests for tapshex.csvreader."""

import os
from pathlib import Path
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader
from pprint import pprint


def test_csv2json(capsys):
    """From open CSV file, convert to JSON."""
    HEREDIR = Path(__file__).resolve().parent 
    config_dict = tapshex_config()
    csvfile_str = Path(HEREDIR).joinpath("dctap.csv").read_text()
    json_obj = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    # assert Path(HEREDIR).joinpath("dctap.csv").exists()
    # # expected_output =
    with capsys.disabled():
        print()
        pprint(json_obj)
