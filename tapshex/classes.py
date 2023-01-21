"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, looks_like_uri_or_curie


@dataclass
class StatementTemplate(TAPStatementTemplate):
    """Subclass of DCTAP class TAPStatementTemplate."""

    minoccurs: str = ""
    maxoccurs: str = ""
    mininclusive: str = ""
    maxinclusive: str = ""
    minexclusive: str = ""
    maxexclusive: str = ""
    minlength: str = ""
    maxlength: str = ""


@dataclass
class Shape(TAPShape):
    """Subclass of DCTAP aclass TAPShape."""

    closed: str = ""
    extra: str = ""
    start: str = ""
