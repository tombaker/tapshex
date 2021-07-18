"""@@@"""

# Schema attributes
def get_schema_attributes(schema):
    """@@@"""
    return {attrib for attrib in schema}

def test_get_schema_attributes():
    """@@@"""
    attributes = get_schema_attributes(SCHEMA)
    assert "@context" in attributes
    assert "shapes" in attributes
    assert "type" in attributes
    assert isinstance(SCHEMA["@context"], str)
    assert isinstance(SCHEMA["shapes"], list)
    assert isinstance(SCHEMA["type"], str)

# Shape list
def get_shape_list(schema):
    """@@@"""
    return [shape for shape in schema["shapes"]]

def test_get_shape_list():
    """@@@"""
    shape_list = get_shape_list(SCHEMA)
    assert len(shape_list) == 2




SCHEMA = {
  "type": "Schema",
  "shapes": [
    {
      "type": "Shape",
      "id": "http://ex.example/#author",
      "expression": {
        "type": "TripleConstraint",
        "predicate": "http://ex.example/#nickname",
        "valueExpr": {
          "type": "NodeConstraint",
          "pattern": "John*"
        }
      }
    },
    {
      "type": "Shape",
      "id": "http://ex.example/#book",
      "expression": {
        "type": "EachOf",
        "expressions": [
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/creator",
            "valueExpr": {
              "type": "ShapeAnd",
              "shapeExprs": [
                {
                  "type": "NodeConstraint",
                  "nodeKind": "iri"
                },
                "http://ex.example/#author"
              ]
            },
            "min": 1,
            "max": 1,
            "annotations": [
              {
                "type": "Annotation",
                "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
                "object": {
                  "value": "Author"
                }
              },
              {
                "type": "Annotation",
                "predicate": "http://www.w3.org/2000/01/rdf-schema#comment",
                "object": {
                  "value": "Writer of the book"
                }
              }
            ]
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/date",
            "valueExpr": {
              "type": "NodeConstraint",
              "datatype": "http://www.w3.org/2001/XMLSchema#date"
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/subject",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "type": "IriStem",
                  "stem": "https://id.loc.gov"
                }
              ]
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#status",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "value": "confidential"
                }
              ]
            }
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#description",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "type": "Language",
                  "languageTag": "fr"
                },
                {
                  "type": "Language",
                  "languageTag": "it"
                },
                {
                  "type": "Language",
                  "languageTag": "en"
                }
              ]
            },
            "min": 1,
            "max": 1
          },
          {
            "type": "TripleConstraint",
            "predicate": "http://ex.example/#colors",
            "valueExpr": {
              "type": "NodeConstraint",
              "values": [
                {
                  "value": "blue"
                },
                {
                  "value": "green"
                }
              ]
            }
          },
        ]
      },
      "annotations": [
        {
          "type": "Annotation",
          "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
          "object": {
            "value": "Book"
          }
        }
      ]
    }
  ],
  "@context": "http://www.w3.org/ns/shex.jsonld"
}
