"""Compute default config dict."""

import pytest
from dctap.config import _initialize_config_dict
from tapshex.classes import Shape, StatementTemplate


def test_initialize_config_dict(capsys):
    """Compute default config dict from TAP classes and add placeholders."""
    expected_output = {
        'csv_elements': [
            '_dot',
            'shapeID',
            'shapeLabel',
            'closed',
            'extra',
            'start',
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
        ],
        "default_shape_identifier": "default",
        'element_aliases': {
             'closed': 'closed',
             'extra': 'extra',
             'mandatory': 'mandatory',
             'maxexclusive': 'maxexclusive',
             'maxinclusive': 'maxinclusive',
             'maxlength': 'maxlength',
             'maxoccurs': 'maxoccurs',
             'minexclusive': 'minexclusive',
             'mininclusive': 'mininclusive',
             'minlength': 'minlength',
             'minoccurs': 'minoccurs',
             'note': 'note',
             'propertyid': 'propertyID',
             'propertylabel': 'propertyLabel',
             'repeatable': 'repeatable',
             'shapeid': 'shapeID',
             'shapelabel': 'shapeLabel',
             'start': 'start',
             'valueconstraint': 'valueConstraint',
             'valueconstrainttype': 'valueConstraintType',
             'valuedatatype': 'valueDataType',
             'valuenodetype': 'valueNodeType',
             'valueshape': 'valueShape'
        },
        "extra_element_aliases": {},
        "extra_shape_elements": [],
        "extra_statement_template_elements": [],
        "extra_value_node_types": [],
        "picklist_elements": [],
        "picklist_item_separator": " ",
        "prefixes": {},
        'shape_elements': ['shapeID', 'shapeLabel', 'closed', 'extra', 'start'],
        'statement_template_elements': [
            'dot_placeholder',
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
    }
    real_output = _initialize_config_dict(Shape, StatementTemplate)
    # assert real_output == expected_output
    assert sorted(real_output["csv_elements"]) == sorted(expected_output["csv_elements"])
    assert sorted(real_output["element_aliases"]) == sorted(expected_output["element_aliases"])
    # with capsys.disabled():
    #     print()
    #     print("csv_elements:")
    #     print(real_output["csv_elements"])


#        'element_aliases', 'extra_element_aliases', 'extra_shape_elements', 'extra_statement_template_elements', 'extra_value_node_types', 'picklist_elements', 'picklist_item_separator', 'prefixes', 'shape_elements', 'statement_template_elements'])
