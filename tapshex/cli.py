"""DC Tabular Application Profiles (DCTAP) to ShEx

Modeled on https://github.com/dcmi/dctap-python/blob/main/dctap/cli.py
"""

import sys
import json as j
from ruamel.yaml import YAML
import click
from .defaults import DEFAULT_CONFIGFILE_NAME, DEFAULT_HIDDEN_CONFIGFILE_NAME
from dctap.config import get_config, write_configfile
from dctap.csvreader import csvreader
from dctap.inspect import pprint_tapshapes, print_warnings
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
    Write an editable configuration file:
    $ dctap init                           # Write dctap.yaml
    $ dctap init --hidden                  # Write .dctaprc
    \b
    Parse a CSV and generate a normalized view:
    $ dctap read x.csv                     # Output as plain text
    $ dctap read --json x.csv              # Output as JSON
    $ dctap read --yaml x.csv              # Output as YAML
    $ dctap read --expand-prefixes x.csv   # Expand prefixes
    $ dctap read --warnings x.csv          # Show warnings
    $ dctap read --config ../taprc x.csv   # Point to a configfile
    """


@cli.command()
@click.option("--hidden", default=False, help="Write as dot file [.tapshexrc]")
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context, hidden):
    """Write config file [default: tapshex.yml]."""
    if hidden:
        configfile = DEFAULT_HIDDEN_CONFIGFILE_NAME
    else:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile)


@cli.command()
@click.argument("csvfile_obj", type=click.File(mode="r", encoding="utf-8-sig"))
@click.option("--config", type=click.Path(exists=True), help="Alternative config file")
@click.option("--expand-prefixes", is_flag=True, help="Expand compact IRIs")
@click.option("--warnings", is_flag=True, help="Print warnings to stderr")
@click.option("--json", is_flag=True, help="Print JSON to stdout")
@click.option("--yaml", is_flag=True, help="Print YAML to stdout")
@click.help_option(help="Show help and exit")
@click.pass_context
def read(context, csvfile_obj, config, expand_prefixes, warnings, json, yaml):
    """Normalize TAP to text, JSON, YAML, ShExC, or ShExJ, optionally with warnings."""
    # pylint: disable=too-many-locals,too-many-arguments

    config_dict = get_config(configfile_name=config)
    (tapshapes_dict, warnings_dict) = csvreader(csvfile_obj, config_dict)
    if expand_prefixes:
        tapshapes_dict = expand_uri_prefixes(tapshapes_dict, config_dict)

    if json and yaml:
        # Quick fix for mutually exclusive options, a better fix in future.
        echo = stderr_logger()
        echo.warning("Please use either --json or --yaml")
        click.Context.exit(0)

    if json:
        json_output = j.dumps(tapshapes_dict, indent=4)
        print(json_output)
        if warnings:
            print_warnings(warnings_dict)

    if yaml:
        y = YAML()
        y.indent(mapping=2, sequence=4, offset=2)
        y.dump(tapshapes_dict, sys.stdout)
        if warnings:
            print_warnings(warnings_dict)

    if not (json or yaml):
        pprint_output = pprint_tapshapes(tapshapes_dict, config_dict)
        for line in pprint_output:
            print(line, file=sys.stdout)
        if warnings:
            print_warnings(warnings_dict)


@click.argument("csvfile_obj", type=click.File(mode="r", encoding="utf-8-sig"))
@click.option("--config", type=click.Path(exists=True), help="Alternative config file")
@click.option("--expand-prefixes", is_flag=True, help="Expand compact IRIs")
@click.option("--warnings", is_flag=True, help="Print warnings to stderr")
@click.option("--shexj", is_flag=True, help="Print ShExJ to stdout")
@click.help_option(help="Show help and exit")
@click.pass_context
def shexify(context, csvfile_obj, config, expand_prefixes, warnings, shexj):
    """Normalize TAP to ShExC or ShExJ, optionally with warnings."""
