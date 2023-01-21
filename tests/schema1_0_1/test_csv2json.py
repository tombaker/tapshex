"""Tests for tapshex.csvreader."""

from pathlib import Path
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader


def test_csv2json():
    """From open CSV file, convert to JSON."""
    config_dict = tapshex_config()
    csvfile_obj = Path("dctap.csv").open(encoding="utf-8")
    json_obj = tapshex_csvreader(csvfile_obj, config_dict)
    print(json_obj)
    print(json_obj)
    print(json_obj)
    print(json_obj)
    print(json_obj)
