"""Tapshex wrapper for DCTAP CSV reader."""

from dctap.csvreader import csvreader
from tapshex.classes import Shape, StatementTemplate


def tapshex_csvreader(
    csvfile_str=None,
    config_dict=None,
    shape_class=Shape,
    state_class=StatementTemplate,
):
    """From CSV string, return DCTAP shapes dict."""
    # Open file object not passable because cannot be read twice.
    return csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=shape_class,
        state_class=state_class,
    )
