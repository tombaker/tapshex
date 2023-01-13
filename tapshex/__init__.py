"""Generate ShEx from DCTAP instances."""

from dctap.tapclasses import TAPShape, TAPStatementTemplate
from dctap.csvreader import csvreader

__version__ = "0.2.2"

# Keep version number in sync with:
# - https://github.com/tap/tapshex/blob/main/docs/conf.py#L28
#   ../docs/conf.py
# - https://github.com/tap/tapshex/blob/main/dctap/cli.py#L20
#   ../dctap/cli.py
