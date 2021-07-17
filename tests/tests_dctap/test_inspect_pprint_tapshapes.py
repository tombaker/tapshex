"""Pretty-print tapshape dicts to console."""

import pytest
from dataclasses import asdict
from textwrap import dedent
from dctap.tapclasses import TAPShape, TAPStatementConstraint
from dctap.inspect import pprint_tapshapes


SHAPES_DICT = {'shapes': [{'sh_warnings': {},
             'shapeID': ':a',
             'shapeLabel': None,
             'statement_constraints': [{'mandatory': False,
                                        'note': None,
                                        'propertyID': 'dct:creator',
                                        'propertyLabel': None,
                                        'repeatable': True,
                                        'sc_warnings': {},
                                        'valueConstraint': None,
                                        'valueConstraintType': None,
                                        'valueDataType': None,
                                        'valueNodeType': None,
                                        'valueShape': None},
                                       {'mandatory': False,
                                        'note': None,
                                        'propertyID': 'dct:date',
                                        'propertyLabel': None,
                                        'repeatable': True,
                                        'sc_warnings': {},
                                        'valueConstraint': None,
                                        'valueConstraintType': None,
                                        'valueDataType': None,
                                        'valueNodeType': None,
                                        'valueShape': None}]},
            {'sh_warnings': {},
             'shapeID': ':b',
             'shapeLabel': None,
             'statement_constraints': [{'mandatory': None,
                                        'note': None,
                                        'propertyID': 'foaf:name',
                                        'propertyLabel': None,
                                        'repeatable': None,
                                        'sc_warnings': {},
                                        'valueConstraint': None,
                                        'valueConstraintType': None,
                                        'valueDataType': None,
                                        'valueNodeType': None,
                                        'valueShape': None}]}]}


