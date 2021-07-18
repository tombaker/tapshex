"""Convert shapeLabel."""

def _convert_shape_shapelabel(shape):
    """@@@"""
    if shape.get("shapeLabel"):
        sh_annotation = dict()
        sh_annotation["type"] = "Annotation"
        sh_annotation["predicate"] = "http://www.w3.org/2000/01/rdf-schema#label"
        sh_annotation["object"] = dict()
        sh_annotation["object"]["value"] = shape.get("shapeLabel")
    return sh_annotation

def test_shape_shapelabel():
    """@@@"""
    input_dict = {
        "shapeID": ":creator",
        "shapeLabel": "Book",
    }
    output_dict = {
        "type": "Annotation",
        "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
        "object": {
            "value": "Book"
        }
    }
    assert _convert_shape_shapelabel(input_dict) == output_dict

