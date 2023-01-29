from jinja2 import Template
from pprint import pprint
from .template import SHEX_JINJA
from pyshexc.parser_impl.generate_shexj import parse
import json


def tapdict_to_shexc(dctap_as_dict=None, shex_template=None):
    """Given TAP as Python dict, generate ShExC schema."""
    template = Template(SHEX_JINJA)
    return template.render(dctap_as_dict)


def shexc_to_shexj(shexc_schema=None):
    """Given ShExC schema, generate ShExJ schema."""
    shexj_schema=parse(shexc_schema)._as_json
    return json.loads(shexj_schema)
