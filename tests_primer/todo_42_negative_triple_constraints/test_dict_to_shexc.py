"""Convert from Python dict to ShExC schema string: using ../../tapshex/template.py."""

# pylint: disable=unused-import,unused-argument,import-error
from pathlib import Path
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA

def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "ex:": "http://ex.example/#",
        },
        "shapes": [
            {
                "shapeID": "my:SolitaryIssueShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:state",
                        "valueConstraint": ["ex:unassigned", "ex:assigned"],
                        "valueConstraintType": "picklist",
                    },
                    {
                        "propertyID": "ex:component",
                        "minoccurs": "0",
                    }
                ],
            }
        ],
        "warnings": {
            "my:SolitaryIssueShape": {}
        },
    }
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    # for line in [
    #     "PREFIX my: <http://my.example/#>",
    #     "PREFIX ex: <http://ex.example/#>",
    #     "my:SolitaryIssueShape {",
    #     "  ex:state [ex:unassigned ex:assigned]",
    #     "  ex:component {0,}",
    #     "}",
    # ]:
    #     assert line in shexc_output
    
    with capsys.disabled():
        print()
        print(shexc_output)
        print()
        HEREDIR = Path(__file__).resolve().parent
        for line in Path(HEREDIR).joinpath("primer.shexc").read_text().splitlines():
            print(line)

    # Or should it be: ex:component . {0} ;

