"""
Convert from Python dict to ShExC schema string:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.2 Triple Constraints 
  - https://shexspec.github.io/primer/#tripleConstraints

1. Use expected_dict (from test_csv_to_dict.py) => input_dctap_dict.
2. Comment out 'for line in...'.
3. Comment out capsys output.
4. Run pytest 
5. Compare generated ShExC to ./primer.shexc
6. Use generated ShExC to replace lines to 'for lines in...'.
"""

# pylint: disable=unused-import,unused-argument,import-error
from textwrap import dedent
import pytest
from tapshex.shexify import tapdict_to_shexc
from tapshex.template import SHEX_JINJA


@pytest.mark.skip(reason="Needs ValueConstraint Type 'picklist' and ValueShape.")
def test_dict_to_shexc(capsys):
    """Convert from Python dict to ShExC schema string."""
    input_dctap_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "foaf:": "http://xmlns.com/foaf/0.1/",
            "xsd:": "http://www.w3.org/2001/XMLSchema#",
        },
        "shapes": [
            {
                "shapeID": "my:UserShape",
                "statement_templates": [
                    {
                        "propertyID": "foaf:name",
                        "valueDataType": "xsd:string",
                    },
                ],
            }
        ],
        "warnings": {"my:UserShape": {}},
    }
    shexc_output = tapdict_to_shexc(
        dctap_as_dict=input_dctap_dict, shex_template=SHEX_JINJA
    )
    for line in [
        "PREFIX my: <http://my.example/#>",
        "PREFIX foaf: <http://xmlns.com/foaf/0.1/>",
        "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>",
        "my:UserShape {",
        "  foaf:name xsd:string",
        "}",
    ]:
        assert line in shexc_output
    #
    #
    # with capsys.disabled():
    #     print()
    #     print()
    #     print(shexc_output)
