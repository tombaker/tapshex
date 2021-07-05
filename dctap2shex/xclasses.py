"""Classes for Python objects derived from CSV files."""

import re
from dataclasses import dataclass, asdict
from dctap.tapclasses import TAPStatementConstraint, TAPShape
from dctap.utils import is_uri_or_prefixed_uri


@dataclass
class TAPStatementConstraintX(TAPStatementConstraint):
    """A statement constraint, its fields extended from 'dctap' for ShEx."""
    min: str = ""
    max: str = ""


@dataclass
class TAPShapeX(TAPShape):
    """A shape, its fields extended from 'dctap' for ShEx."""

    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    start: bool = False
    closed: bool = False

    def validate2(self, config_dict=None):
        """Normalize values where required."""
        self._start_closed_have_supported_boolean_values()
        return True

    def _start_closed_have_supported_boolean_values(self):
        """Booleans take true/false (case-insensitive) or 1/0, default None."""
        valid_values_for_true = ["true", "1"]
        valid_values_for_false = ["false", "0"]
        valid_values = valid_values_for_true + valid_values_for_false + [None]
        # pylint: disable=singleton-comparison
        if self.closed != None:
            # breakpoint(context=5)
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
