"""Tapshex wrappers for DCTAP configuration functions."""

from dctap.config import get_config
from tapshex.classes import Shape, StatementTemplate
from tapshex.defaults import DEFAULT_CONFIGYAML, DEFAULT_CONFIGFILE


def tapshex_config(
    nondefault_configyaml_str=None,
    nondefault_configfile_name=None,
    default_configyaml_str=DEFAULT_CONFIGYAML,
    default_configfile_name=DEFAULT_CONFIGFILE,
    default_shape_class=Shape,
    default_state_class=StatementTemplate,
):
    """Return DCTAP configuration dict initialized with Tapshex classes."""
    return get_config(
        nondefault_configyaml_str=nondefault_configyaml_str,
        nondefault_configfile_name=nondefault_configfile_name,
        default_configyaml_str=default_configyaml_str,
        default_configfile_name=default_configfile_name,
        default_shape_class=default_shape_class,
        default_state_class=default_state_class,
    )
