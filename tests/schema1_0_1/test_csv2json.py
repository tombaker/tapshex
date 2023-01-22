"""Tests for tapshex.csvreader."""

import os
from pathlib import Path
import pytest
from dctap.csvreader import csvreader
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

def test_csv2json(capsys):
    """From open CSV file, convert to JSON."""
    heredir = Path(__file__).resolve().parent 
    config_dict = tapshex_config()
    csvfile_obj = Path(heredir).joinpath("dctap.csv").open(encoding="utf-8")
    # json_obj = tapshex_csvreader(csvfile_obj, config_dict)
    json_obj = csvreader(
        open_csvfile_obj=csvfile_obj, 
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert Path(heredir).joinpath("dctap.csv").exists()
    with capsys.disabled():
        print()
        print(heredir)
        print(Path(heredir).joinpath("dctap.csv"))
        print(Path(Path(heredir)))
