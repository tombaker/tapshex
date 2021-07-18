"""Convert list of TAPShapeX instances into ShEx Schema."""

from typing import Union, List, Optional
from jsonasobj import as_json, loads
from dctap2shex.xclasses import TAPShapeX, TAPStatementConstraintX
from ShExJSG import Schema
from ShExJSG.ShExJ import Shape, IRIREF, TripleConstraint, NodeConstraint, shapeExpr, EachOf


def get_shex_nc(tap_sc: TAPStatementConstraintX) -> Optional[shapeExpr]:
    """Generate ShEx node constraint from CSV triple constraint if necessary."""
    rval = None

    def get_nc() -> NodeConstraint:
        return rval if rval else NodeConstraint()

    nc = get_nc()
    if tap_sc.valueNodeType:
        nc.nodeKind = tap_sc.valueNodeType.lower()
    return nc


