"""Convert statement constraints of value constraint type "picklist"."""


def _convert_sc_note_to_annotation(sc):
    """NOTE: Resulting annotation to be appended to list tc["annotations"]."""
    if sc.get("note"):
        annotation = dict()
        annotation["type"] = "Annotation"
        annotation["predicate"] = "http://www.w3.org/2000/01/rdf-schema#comment"
        annotation["object"] = dict()
        annotation["object"]["value"] = sc.get("note")
    return annotation


def test_convert_picklist_of_two_literals():
    """@@@"""
    input_dict = {"note": "Writer of the book"}
    output_dict = {
        "type": "Annotation",
        "predicate": "http://www.w3.org/2000/01/rdf-schema#comment",
        "object": {"value": "Writer of the book"},
    }
    assert _convert_sc_note_to_annotation(input_dict) == output_dict
