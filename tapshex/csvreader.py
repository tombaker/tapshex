"""Tapshex wrapper for DCTAP CSV reader."""

from dctap.csvreader import csvreader
from tapshex.classes import Shape, StatementTemplate


def tapshex_csvreader(
    open_csvfile_obj=None,
    config_dict=None,
    shape_class=Shape,
    state_class=StatementTemplate,
):
    """From open CSV file object, return Tapshex shapes dict."""
    return csvreader(
        open_csvfile_obj=open_csvfile_obj,
        config_dict=config_dict,
        shape_class=shape_class,
        state_class=state_class,
    )
