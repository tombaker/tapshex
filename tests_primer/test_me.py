from textwrap import dedent
from jinja2 import Template
import pytest
from tapshex.shexify import tapdict_to_shexc

@pytest.mark.skip
def test_me(capsys):
    """@@@"""
    SHEX_JINJA = """
    {%- for state in states %}
    {%- if state.valueShape %} @{{state.valueShape}}{% endif -%}
    {%- endif -%}
    {%- endfor %}
    """
    states = [
        {
            'propertyID': 'ex:reportedBy', 
            'valueShape': 'my:UserShape'
        }
    ]

    expected_output = """\
    my:IssueShape {
      ex:state [ex:unassigned ex:assigned];
      ex:reportedBy @my:UserShape
    }
    """

    with capsys.disabled():
        print(tapdict_to_shexc(dctap_as_dict=states, shex_template=SHEX_JINJA))

#        {
#            'propertyID': 'ex:state',
#            'valueConstraint': ['ex:unassigned', 'ex:assigned'],
#            'valueConstraintType': 'picklist'
#        }, {

#    {{state.property}} {{state.propertyID}}

#    {%- if state.valueConstraint %}
#         {%- if statement.valueConstraintType == "picklist" %}
#             {%- for vc in statement.valueConstraint -%}
#               {{vc}}
#             {%- endfor -%}
#         {%- endif -%} }

#    {%- if not loop.last -%} ;{%- endif -%}

@pytest.mark.skip
def huh():
    if statement.valueConstraint:
        if statement.valueConstraintType == "picklist":
            print("[")
            for vc in statement.valueConstraint:
                print(vc)
            print("]")


