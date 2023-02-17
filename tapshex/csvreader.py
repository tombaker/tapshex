"""Tapshex wrapper for DCTAP CSV reader."""

from dctap.csvreader import csvreader
from tapshex.classes import Shape, StatementTemplate


def dctap_csvreader(
    csvfile_str=None,
    config_dict=None,
    shape_class=Shape,
    state_class=StatementTemplate,
):
    """From CSV string, return DCTAP shapes dict."""
    # Open file object not passable because it can only be read once.
    tapshapes = csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=shape_class,
        state_class=state_class,
    )
    return tapshapes


def tapshex_postprocess(tapshapes):
    """Postprocess DCTAP shapes dict."""
    for shape in tapshapes.values():
        shape.postprocess()
    return tapshapes


def _convert_sc_mandatory_to_sc_min(sc):
    """If mandatory "true" or "false", set "max" accordingly, delete mandatory."""
    if sc.get("mandatory"):
        mand = sc["mandatory"].lower()
        if mand == "true":
            sc["min"] = 1
        elif mand == "false":
            sc["min"] = 0
    del sc["mandatory"]
    return sc


def _convert_sc_repeatable_to_sc_max(sc):
    """If repeatable "true" or "false", set "max" accordingly, delete repeatable."""
    if sc.get("repeatable"):
        repeat = sc["repeatable"].lower()
        if repeat == "true":
            sc["max"] = -1
        elif repeat == "false":
            sc["max"] = 1
    del sc["repeatable"]
    return sc
