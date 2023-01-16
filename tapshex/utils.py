"""Convert mandatory to min."""


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
