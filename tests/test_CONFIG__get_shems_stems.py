"""Get lists of shape / statement template elements from dataclasses."""

import pytest
from dctap.config import _get_shems, _get_stems
from tapshex.classes import Shape, StatementTemplate


def test_get_Shape_elements_when_no_config_dict_specified():
    """List Shape elements (minus shape_warns and state_list)."""
    expected = ['shapeID', 'shapeLabel', 'closed', 'extra', 'start']
    assert _get_shems(Shape) == expected


def test_get_StatementTemplate_elements_when_no_config_dict_specified():
    """List StatementTemplate elements (minus state_warns)."""
    expected = [
        '_dot',
        'propertyID',
        'propertyLabel',
        'mandatory',
        'repeatable',
        'valueNodeType',
        'valueDataType',
        'valueConstraint',
        'valueConstraintType',
        'valueShape',
        'note',
        'minoccurs',
        'maxoccurs',
        'mininclusive',
        'maxinclusive',
        'minexclusive',
        'maxexclusive',
        'minlength',
        'maxlength'
    ]
    assert sorted(_get_stems(StatementTemplate)) == sorted(expected)
