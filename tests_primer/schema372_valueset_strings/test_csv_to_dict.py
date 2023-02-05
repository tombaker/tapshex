"""
Convert from CSV string to Python dict:
- uses Jinja template at ../../tapshex/template.py

Here:
- 3.1 Node Constraints: literal datatype
  - Node constraint that identifies datatype of RDF literal.
  - https://shexspec.github.io/primer/#nodeConstraints
"""

# pylint: disable=unused-import,unused-argument,import-error
import pytest
from tapshex.classes import Shape, StatementTemplate
from tapshex.config import tapshex_config
from tapshex.csvreader import tapshex_csvreader

NONDEFAULT_CONFIGYAML_STR = """
prefixes:
    "my:":      "http://my.example/#"
    "ex:":      "http://ex.example/#"
"""

def test_valueConstraintType_picklist_parse(capsys):
    """If valueConstraintType picklist, valueConstraint parsed on whitespace."""
    config_dict = tapshex_config()
    st = StatementTemplate()
    st.propertyID = "dcterms:creator"
    st.valueConstraintType = "picklist_quoted"
    st.valueConstraint = "0 1"
    st._valueConstraintType_picklist_parse(config_dict)
    assert st.valueConstraint == "0 1"
    assert st.valueConstraintType == "picklist_quoted"
    #with capsys.disabled():
    #    from pprint import pprint
    #    pprint(st)

def test_csv_to_dict(capsys):
    """From CSV to Python dict (actual_dict)."""
    config_dict = tapshex_config(nondefault_configyaml_str=NONDEFAULT_CONFIGYAML_STR)
    # fmt: off
    #
    csvfile_str = """\
    shapeID       , propertyID , valueConstraint     , valueConstraintType
    my:IssueShape , ex:state   , unassigned assigned , picklist_quoted
    """
    #
    # fmt: on
    expected_dict = {
        "namespaces": {
            "my:": "http://my.example/#",
            "ex:": "http://ex.example/#",
        },
        "shapes": [
            {
                "shapeID": "my:IssueShape",
                "statement_templates": [
                    {
                        "propertyID": "ex:state",
                        "valueConstraint": ["unassigned", "assigned"],
                        "valueConstraintType": "picklist_quoted",
                    },
                ],
            }
        ],
        "warnings": {"my:IssueShape": {}},
    }
    # pylint: disable=invalid-name
    actual_dict = tapshex_csvreader(
        csvfile_str=csvfile_str,
        config_dict=config_dict,
        shape_class=Shape,
        state_class=StatementTemplate,
    )
    assert isinstance(actual_dict, dict)
    assert isinstance(actual_dict["namespaces"], dict)
    assert actual_dict["namespaces"] == expected_dict["namespaces"]
    assert sorted(actual_dict["shapes"]) == sorted(expected_dict["shapes"])
    assert actual_dict == expected_dict
    # with capsys.disabled():
    #     from pprint import pprint
    #     pprint(actual_dict)
