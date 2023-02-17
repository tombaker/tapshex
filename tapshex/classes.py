"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, looks_like_uri_or_curie


@dataclass
class StatementTemplate(TAPStatementTemplate):
    """StatementTemplate - subclass of DCTAP class TAPStatementTemplate."""

    _dot: bool = True
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
        self._convert_st_mandatory_to_minoccurs()
        self._convert_st_repeatable_to_maxoccurs()
        self._valueConstraintType_picklist_quoted_parse(config_dict)
        self._dot_placeholder()
        return self

    def _dot_placeholder(self):
        """False when dot NOT needed as placeholder triple constraint."""
        triple_constraints = [
            self.mininclusive,
            self.maxinclusive,
            self.minexclusive,
            self.maxexclusive,
            self.minlength,
            self.maxlength,
            self.valueNodeType,
            self.valueDataType,
            self.valueConstraint,
            self.valueConstraintType,
            self.valueShape,
        ]
        self._dot = not any(triple_constraints)
        return self

    def _convert_st_mandatory_to_minoccurs(self):
        """If mandatory "true" or "false", set minoccurs, delete mandatory."""
        if hasattr(self, "mandatory"):
            mand = self.mandatory.lower()
            if mand == "true":
                self.minoccurs = "1"
            elif mand == "false":
                self.minoccurs = "0"
        del self.mandatory
        return self

    def _convert_st_repeatable_to_maxoccurs(self):
        """If repeatable "true" or "false", set maxoccurs, delete repeatable."""
        if hasattr(self, "repeatable"):
            repeat = self.repeatable.lower()
            if repeat == "true":
                self.maxoccurs = "-1"
            elif repeat == "false":
                self.maxoccurs = "1"
        del self.repeatable
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
    """Shape - subclass of DCTAP dataclass TAPShape."""

    closed: str = ""
    extra: str = ""
    start: str = ""
