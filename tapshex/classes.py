"""Subclasses of DCTAP dataclasses."""

import re
from dataclasses import dataclass, field
from typing import List
from .utils import value_is_numeric
from dctap.tapclasses import TAPStatementTemplate, TAPShape
from dctap.utils import coerce_integer, coerce_numeric, is_uri_or_prefixed_uri


@dataclass
class StatementTemplate(TAPStatementTemplate):
    """Extends DCTAP class TAPStatementTemplate."""

    propertyExtra: str = ""
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
        self._convert_boolean_values_to_integers(self)
        self._convert_mandatory_to_minoccurs(self)
        self._convert_repeatable_to_maxoccurs(self)
        self._are_nonnegative_integers(self)
        self._warn_if_values_not_numeric(self)
        return self

    def _convert_boolean_values_to_integers(self):
        """Converts boolean values to integers."""
        elements_that_take_boolean_values = { "propertyExtra": self.propertyExtra }
        for element in self.elements_that_take_boolean_values:
            value = self.get(element)
            if value:
                if value.lower() == "true":
                    self[element] = 1
                elif value.lower() == "false":
                    self[element] = 0

    def _convert_mandatory_to_minoccurs(self):
        """If mandatory has value, replace with minOccurs."""
        if self.mandatory:
            mand = self.mandatory.lower()
            if mand == "true":
                self.minOccurs = 1 
            elif mand == "false":
                self.minOccurs = 0
        del self.mandatory
        return self

    def _convert_repeatable_to_maxoccurs(self):
        """If repeatable has value, replace with maxOccurs."""
        if self.repeatable:
            repeat = self.repeatable.lower()
            if repeat == "true":
                self.maxOccurs = -1
            elif repeat == "false":
                self.maxOccurs = 1
        del self.repeatable
        return self

    def _are_nonnegative_integers(self):
        """Four elements take values that must be nonnegative integers."""
        elements_that_take_nonnegative_integers = {
            "minOccurs": self.minOccurs,
            "maxOccurs": self.maxOccurs,
            "minLength": self.minLength,
            "maxLength": self.maxLength,
        }
        for (elem, state_field) in elements_that_take_nonnegative_integers.items():
            warning_message = f"Value {repr(state_field)} is not a nonnegative integer"
            state_field = coerce_integer(state_field)
            if isinstance(state_field, int):
                if state_field < 0:
                    self.state_warns[elem] = warning_message
            elif state_field:  # but empty strings should not generate warnings
                self.state_warns[elem] = warning_message
        return self

    def _warn_if_values_not_numeric(self):
        """@@@"""
        elements_that_take_numerical_values = {
            "minInclusive": self.minInclusive,
            "maxInclusive": self.maxInclusive,
            "minExclusive": self.minExclusive,
            "maxExclusive": self.maxExclusive,
        }



@dataclass
class Shape(TAPShape):
    """Extends DCTAP class TAPShape."""

    closed: str = ""
    start: str = ""

    def _convert_boolean_values_to_integers(self):
        """Converts boolean values to integers."""
        elements_that_take_boolean_values = {
            "closed": self.closed,
            "start": self.start,
        }
        for element in self.elements_that_take_boolean_values:
            value = self.get(element)
            if value:
                if value.lower() == "true":
                    self[element] = 1
                elif value.lower() == "false":
                    self[element] = 0
