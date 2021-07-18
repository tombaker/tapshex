"""@@@"""

def _start_closed_have_supported_boolean_values(self):
    """Booleans take true/false (case-insensitive) or 1/0, default None."""
    valid_values_for_true = ["true", "1"]
    valid_values_for_false = ["false", "0"]
    valid_values = valid_values_for_true + valid_values_for_false + [None]
    # pylint: disable=singleton-comparison
    if self.closed != None:
        mand = self.closed.lower()
        if mand not in valid_values and mand != "":
            self.sc_warnings[
                "closed"
            ] = f"{repr(self.closed)} is not a supported Boolean value."
        if mand in valid_values_for_true:
            self.closed = True
        elif mand in valid_values_for_false:
            self.closed = False
    if self.start != None:
        # breakpoint(context=5)
        repeat = self.start.lower()
        if repeat not in valid_values and repeat != "":
            self.sc_warnings[
                "start"
            ] = f"{repr(self.start)} is not a supported Boolean value."
        if repeat in valid_values_for_true:
            self.start = True
        elif repeat in valid_values_for_false:
            self.start = False
    return self
