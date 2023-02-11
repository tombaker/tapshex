"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, looks_like_uri_or_curie


@dataclass
class StatementTemplate(TAPStatementTemplate):
    """Subclass of DCTAP class TAPStatementTemplate."""

    dot_placeholder: str = "."
    minoccurs: str = ""
    maxoccurs: str = ""
    mininclusive: str = ""
    maxinclusive: str = ""
    minexclusive: str = ""
    maxexclusive: str = ""
    minlength: str = ""
    maxlength: str = ""

    def normalize(self, config_dict):
        """Normalizes specific fields."""
        super(StatementTemplate, self).normalize(config_dict)
        self._valueConstraintType_picklist_quoted_parse(config_dict)
        self._dot_placeholder_required()
        return self

    def _dot_placeholder_required(self):
        """If just one of a list or set of values is True, return True."""
        if any([
            self.propertyID,
            self.valueNodeType,
            self.valueDataType,
            self.valueConstraint,
            self.valueShape,
            self.minoccurs,
            self.maxoccurs,
            self.mininclusive,
            self.maxinclusive,
            self.minexclusive,
            self.maxexclusive,
            self.minlength,
            self.maxlength,
        ]):
            self.dot_placeholder = ""
        return self

    def _valueConstraintType_picklist_quoted_parse(self, config_dict):
        """valueConstraintType "picklist": split valueConstraint on item separator."""
        self.valueConstraintType = self.valueConstraintType.lower()
        sep = config_dict.get("picklist_item_separator", " ")
        if self.valueConstraintType == "picklist_quoted":
            if self.valueConstraint:
                self.valueConstraint = self.valueConstraint.split(sep)
                self.valueConstraint = [x.strip() for x in self.valueConstraint if x]
        return self

@dataclass
class Shape(TAPShape):
    """Subclass of DCTAP aclass TAPShape."""

    closed: str = ""
    extra: str = ""
    start: str = ""
