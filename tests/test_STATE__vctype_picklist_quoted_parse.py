"""Convert mandatory to minoccurs."""

import pytest
from pprint import pprint
from tapshex.config import tapshex_config
from tapshex.classes import StatementTemplate

@pytest.mark.skip(reason="Safely surround in quotes")
def test_convert_st_mandatory_to_max_true(capsys):
    """If mandatory "true", set minoccurs to "-1", delete mandatory."""
    config_dict = tapshex_config()
    st = StatementTemplate()
    st.valueconstraint = "[one two]"
    st.valueconstrainttype = "picklist_quoted"
    assert st.valueconstraint == "[one two]"
    assert st.valueconstrainttype == "picklist_quoted"
    #st._convert_st_mandatory_to_minoccurs()
    #assert not st.mandatory
    #assert st.minoccurs == "1"
    with capsys.disabled():
        print()
        pprint(st)

