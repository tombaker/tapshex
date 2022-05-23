.. _literal_constraining_facets:

Literal constraining facets
...........................

ShEx supports the use of `XML Schema constraining facets <https://www.w3.org/TR/xmlschema-2/#rf-facets>`_, which include constraints on numeric values and constraints on strings. While **tap2shex** could be further extended to support this entire set of facets, it already supports a subset:

- ``MinInclusive`` / ``MaxInclusive``, which are used to define a range within which a numeric value must fall.
- ``MinLength`` / ``MaxLength``, which are used to define a minimum and maximum length of a string value.

The string contraining facet ``pattern`` is already `supported by dctap <https://dctap-python.readthedocs.io/en/latest/elements/valueConstraintType/Pattern/index.html>`_ by using a regular expression with **valueConstraint** and the keyword "pattern" with **valueConstraintType**.

