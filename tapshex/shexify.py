from jinja2 import Template
from pprint import pprint
from pyshexc.parser_impl.generate_shexj import parse
from .template import SHEX_JINJA
import json


def shexify(dctap_as_dict=None, shex_template=None):
    """Given Python dict as output from DCTAP, generate ShExC schema."""

    template = Template(SHEX_JINJA)
    return template.render(dctap_as_dict)


def shexjfy(shexc_schema=None):
    """@@@"""
    shexj_schema=parse(shexc_schema)._as_json
    parsed = json.loads(shexj_schema)
    for line in shexc_schema.splitlines():
        print(line)

