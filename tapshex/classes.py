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
        """Inherits from and extends TAPStatementTemplate.normalize."""
        super().normalize(config_dict)
        self._convert_booleans()
        self._convert_mandatory_to_minoccurs()
        self._convert_repeatable_to_maxoccurs()
        self._try_to_coerce_nonnegative_integers()
        self._try_to_coerce_numbers()
        return self

    def _convert_booleans(self):
        """Convert booleans to integers."""
        boolean_elements = [ "propertyExtra" ]
        for elem in boolean_elements:
            value = getattr(self, elem)
            if value:
                if value.lower() == "true" or value == "1":
                    setattr(self, elem, 1)
                elif value.lower() == "false" or value == "0":
                    setattr(self, elem, 0)

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

    def _try_to_coerce_nonnegative_integers(self):
        """Four elements take values that must be nonnegative integers."""
        integer_elements = [
            "minOccurs",
            "maxOccurs",
            "minLength",
            "maxLength"
        ]
        for elem in integer_elements:
            actual_value = getattr(self, elem)
            warning_message = f"Value {repr(actual_value)} is not a nonnegative integer."
            coerced_value = coerce_integer(actual_value)
            if isinstance(coerced_value, int):
                if coerced_value < 0:
                    self.state_warns[elem] = warning_message
            elif coerced_value:  # though empty strings should not generate warnings
                self.state_warns[elem] = warning_message
        return self

    def _try_to_coerce_numbers(self):
        """Four elements take values that must be integers or floats."""
        numerical_elements = [
            "minInclusive",
            "maxInclusive",
            "minExclusive",
            "maxExclusive"
        ]
        for elem in numerical_elements:
            actual_value = getattr(self, elem)
            warning_message = f"Value {repr(actual_value)} is not a number."
            if actual_value and not value_is_numeric(actual_value):
                try:
                    setattr(self, elem, int(actual_value))
                except ValueError:
                    try:
                        setattr(self, elem, float(actual_value))
                    except ValueError:
                        self.state_warns[elem] = warning_message
        return self


@dataclass
class Shape(TAPShape):
    """Extends DCTAP class TAPShape."""

    closed: str = ""
    start: str = ""

    def normalize(self, config_dict):
        """Inherits from and extends TAPShape.normalize."""
        super().normalize(config_dict)
        self._convert_booleans()
        return self

    def _convert_booleans(self):
        """Convert booleans to integers."""
        boolean_elements = ["closed", "start"]
        for elem in boolean_elements:
            value = getattr(self, elem)
            if value:
                if value.lower() == "true" or value == "1":
                    setattr(self, elem, 1)
                elif value.lower() == "false" or value == "0":
                    setattr(self, elem, 0)
