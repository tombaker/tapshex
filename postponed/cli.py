"""DC Tabular Application Profiles (DCTAP) to ShEx

Modeled on https://github.com/dcmi/dctap-python/blob/main/dctap/cli.py
"""

import sys
import json as j
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
    """Generate ShEx schema from a Tabular Application Profile (TAP).

    Examples (see https://tapshex.rtfd.io):

    \b
    Write starter config file:
    $ tapshex init                     # write dctap.yaml
    $ tapshex init --hidden            # write .dctaprc
    \b
    Show normalized view of TAP:
    $ tapshex parse x.csv              # output plain text
    $ tapshex parse --tapj x.csv       # output TAP/JSON
    $ tapshex parse --shexc x.csv      # output TAP/ShExC
    $ tapshex parse --shexj x.csv      # output TAP/ShExJ
    $ tapshex parse --warnings x.csv   # also show warnings
    """


@cli.command()
@click.option("--hidden", default=False, help="Write as dot file [.tapshexrc]")
@click.help_option(help="Show help and exit")
@click.pass_context
def init(context, hidden):
    """Write config file [default: tapshex.yaml]."""
    if hidden:
        configfile = DEFAULT_HIDDEN_CONFIGFILE_NAME
    else:
        configfile = DEFAULT_CONFIGFILE_NAME
    write_configfile(configfile)


@cli.command()
@click.argument("csv", type=click.File(mode="r", encoding="utf-8-sig"))
@click.option("--config", type=click.Path(exists=True), help="Nondefault config file")
@click.option("--uris", is_flag=True, help="Expand compact URIs")
@click.option("--warnings", is_flag=True, help="Include warnings")
@click.option("--tapj", is_flag=True, help="View as TAP/JSON")
@click.option("--shexc", is_flag=True, help="View as ShExC")
@click.option("--shexj", is_flag=True, help="View as ShExJ")
@click.help_option(help="Show help and exit")
@click.pass_context
def parse(context, csv, config, uris, warnings, tapj, shexc, shexj):
    """View TAP/TXT (default), TAP/JSON, ShExC, or ShExJ, optionally with warnings."""
    # pylint: disable=too-many-locals,too-many-arguments

    if config:
        config_dict = get_config(configfile_name=config)
    else:
        config_dict = get_config()
    tapshapes_dict = csvreader(csv, config_dict)

    if expand_prefixes:
        tapshapes_dict = expand_uri_prefixes(tapshapes_dict, config_dict)

    # if (tapj and shexc) or (tapj and shexj) or (shexc and shexj):
    #     echo = stderr_logger()
    #     echo.warning("Options tapj, shexc, and shexj are mutually exclusive - re-try.")
    #     click.Context.exit(0)

    # if tapj:
    #     if not warnings:
    #         del tapshapes_dict["warnings"]
    #     json_output = j.dumps(tapshapes_dict, indent=2)
    #     print(json_output)
    # elif shexc:
    #     print("Placeholder for ShExC output.")
    # elif shexj:
    #     print("Placeholder for ShExJ output.")
    # else:
    #     pprint_output = pprint_tapshapes(tapshapes_dict, config_dict)
    #     for line in pprint_output:
    #         print(line, file=sys.stdout)
    #     if warnings:
    #         print_warnings(tapshapes_dict["warnings"])
