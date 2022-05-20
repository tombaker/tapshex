.. _dctap_and_shex:

ShEx features not supported by DCTAP
------------------------------------

The `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_ is a sophisticated language for describing RDF graph structures, with a well-defined grammar and a level of expressivity beyond what is attainable in a two-dimensional table. The following comparison of DCTAP and ShEx assumes familiarity with the basics of ShEx, and its terminology, as described in the `ShEx Primer <https://shexspec.github.io/primer/>`_.

Compared to ShEx, the DCTAP model does not support:

- `Reusable expressions <https://shex.io/shex-primer/#labeled-constraints>`_. In a ShEx schema, one can assign a name to a frequently used set of node constraints (eg, to say: "integer between 1970 and 2022", then reference that name in the context of multiple triple constraints. A triple expression can also be defined and labeled just once, then referenced in multiple shapes (eg, if the subjects of "user" and "employee" shapes are both expected to have names and email addresses). In a DCTAP instance, constraints are repeated in every statement template to which they apply, and statement templates are repeated in every shape to which they apply. In other words, a ShEx schema can be `"DRY" <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, while DCTAP instances are "WET" ("Write Every Time"). Of course, DCTAP can serve as a stepping stone to ShEx, where a wet schema, once generated, can be dried.

- `Inverse triple constraints <https://shex.io/shex-primer/#inverse-properties>`_. In DCTAP, statement templates only ever describe "outgoing triples" --- statements about the subject of a given shape. ShEx, however, can also describe "incoming triples" --- statements of which the node of interest is the object.

- `Combinations with AND, OR, or NOT <https://shex.io/shex-primer/#inverse-properties>`_. In ShEx, triple constraints can express choices --- for example, to say that a person must be described either with ``foaf:name`` or with the combination ``foaf:givenName`` and ``foaf:familyName``.

- `Nested shapes <https://shex.io/shex-primer/#nested-shapes>`_. In DCTAP, each shape is assigned an identifier and referenced with that identifier. In ShExC syntax, if a shape is only needed by one other shape, that shape can be embedded, anonymously, within the other.

- `Negative triple constraints <https://shex.io/shex-primer/#negated-properties>`_. In ShEx, a schema can describe triples that `must not` appear in the data.

- `Imported schemas <https://shex.io/shex-primer/#import>`_. A ShEx schema can reference shapes and triple expressions in schemas that are "imported".
