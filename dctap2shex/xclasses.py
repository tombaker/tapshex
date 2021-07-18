"""Classes for Python objects derived from CSV files."""

import re
from dataclasses import dataclass, asdict
from dctap.tapclasses import TAPStatementConstraint, TAPShape
from dctap.utils import is_uri_or_prefixed_uri


@dataclass
class TAPStatementConstraintX(TAPStatementConstraint):
    """A statement constraint, its fields extended from 'dctap' for ShEx."""
    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

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
        # self._start_closed_have_supported_boolean_values()
        return True

