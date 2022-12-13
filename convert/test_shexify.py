"""Convert JSON into ShEx."""

def _mkschema():
    """Makes a ShEx schema lattive with JSON-LD @context."""
    schema = dict()
    schema["type"] = "Schema"
    schema["@context"] = "http://www.w3.org/ns/shex.jsonld"
    schema["shapes"] = list()
    return schema

def test_convert_picklist_of_two_literals():
    """@@@"""
    input_iri = "http://example.org/book" 
    output_dict = {
      "type": "Schema",
      "@context": "http://www.w3.org/ns/shex.jsonld",
      "shapes": [],
    }
    assert _mkschema() == output_dict

