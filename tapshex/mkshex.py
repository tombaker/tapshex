"""Convert list of TAPShape instances into ShEx Schema."""

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

from dctap.tapclasses import TAPShape, TAPStatementTemplate

