{
  "type": "Schema",
  "shapes": [
    {
      "type": "Shape",
      "id": "http://ex.example/#author",            # shapeID
      "annotations": [
          "type": "Annotation",
          "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
          "object": {                               # shapeLabel

----------------------------------------------------------
If just one triple constraint

      "expression": {
        "type": "TripleConstraint",
        "predicate": "http://ex.example/#nickname", # propertyID
        "min:"                                      # mandatory
        "max:"                                      # repeatable
        "valueExpr": {

----------------------------------------------------------
If more than one triple constraint

      "expression": {
        "type": "EachOf",
        "expressions": [
          {
            "type": "TripleConstraint",
            "predicate": "http://purl.org/dc/terms/creator", # propertyID
            "min:"                                  # mandatory
            "max:"                                  # repeatable
            "valueExpr": {
              "type": "ShapeAnd",
              "shapeExprs": [
                {
                  "type": "NodeConstraint",
                  "nodekind": "iri"                 # valueNodeType (if valueShape)
                },
                "http://ex.example/#author"         # valueShape

            "valueExpr": {
              "type": "NodeConstraint",
              "pattern": "John*"                    # pattern
              or
              "datatype": "http://www...."          # valueDataType
              or
              "nodekind":                           # valueNodeType (if no value shape)
              or
              "values": [
                {
                  "type": "IriStem",                # valueConstraint (type: iristem)
                  "stem": "https://id.loc.gov"      # can be more than one
                }
                  or
                {
                  "value": "confidential"           # valueConstraint (type: none)
                }
                  or
                {
                  "type": "Language",               # valueConstraint (type: languageTag)
                  "languageTag": "fr"               # can be more than one
                },{...
                  or
                {
                  "value": "blue"                   # valueConstraint (type: picklist)
                },{...                              # can be more than one

            "annotations": [
              {
                "type": "Annotation",
                "predicate": "http://www.w3.org/2000/01/rdf-schema#label",
                "object": {                        # propertyLabel
                or
                "predicate": "http://www.w3.org/2000/01/rdf-schema#comment",
                "object": {                        # note
