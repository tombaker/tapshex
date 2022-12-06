"""DC Tabular Application Profiles (DCTAP) to ShEx

Modeled on https://github.com/dcmi/dctap-python/blob/main/dctap/cli.py
"""

import sys
import json as j
from ruamel.yaml import YAML
from pprint import pprint
import click
from .defaults import DEFAULT_CONFIGFILE_NAME, DEFAULT_HIDDEN_CONFIGFILE_NAME
from dctap.config import get_config, write_configfile
from dctap.csvreader import csvreader
from dctap.inspect import pprint_tapshapes
from dctap.loggers import stderr_logger
from dctap.utils import expand_uri_prefixes

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.2.1", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """Generate ShEx schema from a tabular application profile

    Examples (see https://tapshex.rtfd.io):

    \b

    """


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


    """Write starter config file [default: tapshex.yml]."""
    if not configfile:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile)

@cli.command()
@click.option(
    "--hidden/--visible",
    default=False,
    help="Write config to hidden file [.tapshexrc].",
)
@click.option(
    "--terse/--verbose",
    default=False,
    help="Omit verbose commentary from config file.",
)
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context, hidden, terse):
    """Write customizable config file [default: tapshex.yml]."""
    if hidden:
        configfile = DEFAULT_HIDDEN_CONFIGFILE_NAME
    else:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile, terse=terse)


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def model(context):
    """Show DCTAP/SHEX model for ready reference"""

    shape_elements = list(asdict(TAPShape()))
    # shape_elements.remove('tc_list')
    state_elements = list(asdict(TAPStatementTemplate()))
    print("DCTAP/SHEX model")
    print("    Shape elements:")
    for element in shape_elements:
        print(f"        {element}")
    print("        Statement Template elements:")
    for element in state_elements:
        print(f"            {element}")