"""@@@"""

def _convert_sc_mandatory_to_sc_min(sc):
    """@@@"""
    if sc.get("mandatory").lower() == "true":
        sc["min"] = 1 
        del sc.mandatory
    else:
        sc["min"] = 0
        del sc.mandatory
    return sc

def _convert_sc_repeatable_to_sc_max(sc):
    """@@@"""
    if sc.get("repeatable").lower() == "true":
        sc.max = -1 
        del sc.repeatable
    else:
        sc.max = 1
        del sc.repeatable
    return sc
