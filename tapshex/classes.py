"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, is_uri_or_prefixed_uri


@dataclass
class StatementTemplate(TAPStatementTemplate):
    """Extends DCTAP class TAPStatementTemplate."""

    minOccurs: str = ""
    maxOccurs: str = ""
    minInclusive: str = ""
    maxInclusive: str = ""
    minExclusive: str = ""
    maxExclusive: str = ""
    minLength: str = ""
    maxLength: str = ""

    def normalize(self, config_dict):
        """Invokes and extends TAPStatementTemplate.normalize."""
        super().normalize()

@dataclass
class Shape(TAPShape):
    """Extends DCTAP class TAPShape."""

    closed: str = ""
    extra: str = ""
    start: str = ""
