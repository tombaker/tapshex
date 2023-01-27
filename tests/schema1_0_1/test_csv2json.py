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
