"""Convert statement constraints of value constraint type "picklist"."""


def _convert_sc_propertylabel_to_annotation(sc):
    """NOTE: Resulting annotation to be appended to list tc["annotations"]."""
    if sc.get("propertyLabel"):
        annotation = {}
        annotation["type"] = "Annotation"
        annotation["predicate"] = "http://www.w3.org/2000/01/rdf-schema#label"
        annotation["object"] = {}
        annotation["object"]["value"] = sc.get("propertyLabel")
    return annotation


def test_convert_picklist_of_two_literals():
    """@@@"""
    input_dict = {
        "propertyID": "dct:creator",
        "propertyLabel": "Author",
    }
    output_dict = {
        "type": "Annotation",
        "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
        "object": {"value": "Author"},
    }
    assert _convert_sc_propertylabel_to_annotation(input_dict) == output_dict
