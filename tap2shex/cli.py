"""DC Tabular Application Profiles (DCTAP) to ShEx"""

import sys
import json as j
from pprint import pprint
from ruamel.yaml import YAML
import click
from dctap.config import get_config, write_configfile
from dctap.inspect import pprint_tapshapes
from dctap.csvreader import csvreader
from dctap.loggers import stderr_logger
from dctap.utils import expand_uri_prefixes
from tap2shex.defaults import DEFAULT_CONFIG_YAML, DEFAULT_CONFIGFILE_NAME

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """DCTAP/JSON to ShEx"""


@cli.command()
@click.argument("csvfile_obj", type=click.File(mode="r", encoding="utf-8-sig"))
@click.option(
    "--configfile", type=click.Path(exists=True), help="Pathname of configuration file."
)
@click.option(
    "--expand-prefixes",
    is_flag=True,
    help="Compact to full IRI with prefixes mapped to namespaces.",
)
@click.option("--warnings", is_flag=True, help="Print warnings to stderr.")
@click.option("--json", is_flag=True, help="Print JSON to stdout.")
@click.help_option(help="Show help and exit")
@click.pass_context
def generate(context, csvfile_obj, configfile, expand_prefixes, warnings, json):
    """Given CSV, generate text or JSON, optionally with warnings."""
    # pylint: disable=too-many-locals,too-many-arguments

    config_dict = get_config(configfile)
    csvreader_output = csvreader(csvfile_obj, config_dict)
    tapshapes_dict, warnings_dict = csvreader_output
    if expand_prefixes:
        tapshapes_dict = expand_uri_prefixes(tapshapes_dict, config_dict)

    if json:
        json_output = j.dumps(tapshapes_dict, indent=4)
        print(json_output)

    # pylint: disable=logging-fstring-interpolation
    if not json:
        pprint_output = pprint_tapshapes(tapshapes_dict, config_dict)
        for line in pprint_output:
            print(line, file=sys.stdout)
        if warnings:
            print("", file=sys.stderr)
            echo = stderr_logger()
            for (shapeid, warns) in warnings_dict.items():
                for (elem, warn_list) in warns.items():
                    for warning in warn_list:
                        echo.warning(f"[{shapeid}/{elem}] {warning}")


@cli.command()
@click.argument("configfile", type=click.Path(), required=False)
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context, configfile):
    """Generate config file [default: tap2shex.yml]."""
    if not configfile:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile)

