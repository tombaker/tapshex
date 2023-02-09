"""DC Tabular Application Profiles (DCTAP) to ShEx

Modeled on https://github.com/dcmi/dctap-python/blob/main/dctap/cli.py
"""

import sys
import json
import click
from tapshex.defaults import DEFAULT_CONFIGFILE
from tapshex.config import tapshex_config
from dctap.config import get_config, write_configfile
from dctap.csvreader import csvreader
from dctap.inspect import pprint_tapshapes, print_warnings
from dctap.loggers import stderr_logger
from dctap.utils import expand_uri_prefixes

# pylint: disable=unused-argument,no-value-for-parameter
# => unused-argument: Allows placeholders for now.
# => no-value-for-parameter: Okay in cli.py


@click.group()
@click.version_option("0.2.3", help="Show version and exit")
@click.help_option(help="Show help and exit")
@click.pass_context
def cli(context):
    """Generate ShEx schema from a Tabular Application Profile (TAP).

    Examples (see https://tapshex.rtfd.io):

    \b
    Write starter config file:
    $ tapshex init                     # write dctap.yaml
    \b
    Show normalized view of TAP:
    $ tapshex parse x.csv              # output plain text
    $ tapshex parse --tapjson x.csv       # output TAP/JSON
    $ tapshex parse --shexc x.csv      # output TAP/ShExC
    $ tapshex parse --warnings x.csv   # also show warnings
    """


@cli.command()
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context):
    """Write config file [default: tapshex.yaml]."""
    configfile = DEFAULT_CONFIGFILE
    write_configfile(configfile)


@cli.command()
@click.argument("csvfile", type=click.Path(exists=True))
@click.option("--config", type=click.Path(exists=True), help="Nondefault config file")
@click.option("--uris", is_flag=True, help="Expand compact URIs")
@click.option("--warnings", is_flag=True, help="Also show warnings")
@click.option("--tapjson", is_flag=True, help="View as TAP/JSON")
@click.option("--shexc", is_flag=True, help="View as TAP/ShExC")
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(context, csvfile, config, uris, warnings, tapjson, shexc):
    """View TAP/TXT (default), TAP/JSON, or ShExC, optionally with warnings."""
    # pylint: disable=too-many-locals,too-many-arguments

    csvfile_str = Path(csvfile).read_text()
    if config:
        config_dict = tapshex_config(configfile_name=config)
    else:
        config_dict = tapshex_config()

    tapshapes_dict = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict
    )
    if expand_prefixes:
        tapshapes_dict = expand_uri_prefixes(tapshapes_dict, config_dict)

    if tapjson:
        if not warnings:
            del tapshapes_dict["warnings"]
        json_output = json.dumps(tapshapes_dict, indent=2)
        print(json_output)
    elif shexc:
        print("Placeholder for ShExC output.")
    else:
        pprint_output = pprint_tapshapes(tapshapes_dict, config_dict)
        for line in pprint_output:
            print(line, file=sys.stdout)
        if warnings:
            print_warnings(tapshapes_dict["warnings"])
