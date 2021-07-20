"""Convert list of TAPShapeX instances into ShEx Schema."""

from typing import Union, List, Optional
from jsonasobj import as_json, loads
from ShExJSG import Schema
from ShExJSG.ShExJ import (
    Shape,
    IRIREF,
    TripleConstraint,
    NodeConstraint,
    shapeExpr,
    EachOf,
)

from .xclasses import TAPShapeX, TAPStatementConstraintX


def get_node_constraint(tap_sc: TAPStatementConstraintX) -> Optional[shapeExpr]:
    """Generate ShEx node constraint from CSV triple constraint if necessary."""

    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    nc = get_nc()
    if tap_sc.valueNodeType:
        #  pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')
        nc.nodeKind = tap_sc.valueNodeType.lower()
#    if tap_sc.valueConstraint:
#        get_nc().values = [tap_sc.valueConstraint]
#    if tap_sc.valueConstraintType:
#        get_nc().datatype = IRIREF(tap_sc.valueConstraintType)
#    if tap_sc.valueShape:
#        if rval:
#            raise ValueError(
#                "Statement constraint cannot have both "
#                "a NodeConstraint and a ValueConstraint"
#            )
#        return IRIREF(tap_sc.valueShape)
#    return rval
    return nc


def add_triple_constraint(shape: Shape, tap_sc: TAPStatementConstraintX) -> None:
    """Interpret TAP statement constraint and add shapeExpr to shape."""

    # pylint: disable=invalid-name
    # two-letter variable names do not conform to snake-case naming style

    # typing.List[typing.Union["EachOf", "OneOf", "TripleConstraint", typing.Union[str, str]]]
    ts = TripleConstraint(
        # Why does a triple constraint need to have a label?
        # id=tap_sc.prop_label,
        predicate=IRIREF(tap_sc.propertyID),
        min=1 if tap_sc.mandatory else 0,
        max=-1 if tap_sc.repeatable else 1,
        valueExpr=get_node_constraint(tap_sc),
    )
    if shape.expression:
        if isinstance(shape.expression, TripleConstraint):
            shape.expression = EachOf(expressions=[shape.expression, ts])
        else:
            shape.expression.expressions.append(ts)
    else:
        shape.expression = ts


def mkshex(shapes: Union[TAPShapeX, List[TAPShapeX]]) -> Schema:
    """Convert list of TAPShapes to ShExJSG Schema object."""

    # pylint: disable=invalid-name
    # One- and two-letter variable names do not conform to snake-case naming style


    if isinstance(shapes, TAPShapeX):
        shapes = [shapes]
    schema = Schema()
    for s in shapes:
        shape_id = IRIREF(s.shapeID)
        if s.start:
            if schema.start:
                print(f"Multiple start shapes: <{schema.start}>, <{shape_id}>")
            else:
                schema.start = shape_id
        shape = Shape(id=shape_id)
        for tap_sc in s.tc_list:
            add_triple_constraint(shape, tap_sc)
        if not schema.shapes:
            schema.shapes = [shape]
        else:
            schema.shapes.append(shape)
    return schema


def mkshexj(schema):
    """Convert ShExJSG Schema object to ShExJ string."""
    schema = mkshex(schema)
    return as_json(schema)
