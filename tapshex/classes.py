"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, is_uri_or_prefixed_uri


@dataclass
class TAPShExStatementTemplate(TAPStatementTemplate):
    """Subclass of DCTAP dataclass TAPStatementTemplate."""

    min: str = ""
    max: str = ""


@dataclass
class TAPShExShape(TAPShape):
    """Subclass of DCTAP dataclass TAPShape."""

    closed: str = ""
