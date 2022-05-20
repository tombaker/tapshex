.. _dctap_and_shex:

ShEx features not supported by DCTAP
------------------------------------

The `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_ is a sophisticated language for describing RDF graph structures, with a well-defined grammar and a level of expressivity beyond what is attainable in a two-dimensional table. The following comparison of DCTAP and ShEx assumes familiarity with the basics of ShEx, and its terminology, as described in the `ShEx Primer <https://shexspec.github.io/primer/>`_.

Compared to ShEx, the DCTAP model does not support:

- **`Reusable expressions <https://shex.io/shex-primer/#labeled-constraints>`_.** In a ShEx schema, one can assign a name to a frequently used set of node constraints (eg, to say: "integer between 1970 and 2022", then reference that name in the context of multiple triple constraints. A triple expression can also be defined and labeled just once, then referenced in multiple shapes (eg, if the subjects of "user" and "employee" shapes are both expected to have names and email addresses). In a DCTAP instance, constraints are repeated in every statement template to which they apply, and statement templates are repeated in every shape to which they apply. In other words, a ShEx schema can be `"DRY" <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, while DCTAP instances are "WET" ("Write Every Time"). Of course, DCTAP can serve as a stepping stone to ShEx, where a wet schema, once generated, can be dried.

- **`Inverse triple constraints <https://shex.io/shex-primer/#inverse-properties>`_.** In DCTAP, statement templates only ever describe "outgoing triples" --- statements about the subject of a given shape. ShEx, however, can also describe "incoming triples" --- statements of which the node of interest is the object.

- **`Combinations with AND, OR, or NOT <https://shex.io/shex-primer/#inverse-properties>`_.** In ShEx, triple constraints can express choices --- for example, to say that a person must be described either with ``foaf:name`` or with the combination ``foaf:givenName`` and ``foaf:familyName``.

- **`Nested shapes <https://shex.io/shex-primer/#nested-shapes>`_.** In DCTAP, each shape is assigned an identifier and referenced with that identifier. In ShExC syntax, if a shape is only needed by one other shape, that shape can be embedded, anonymously, within the other.

- **`Negative triple constraints <https://shex.io/shex-primer/#negated-properties>`_.** In ShEx, a schema can describe triples that `must not` appear in the data.

- **`Imported schemas <https://shex.io/shex-primer/#import>`_.** A ShEx schema can reference shapes and triple expressions in schemas that are "imported".

.. _dctap_shex_extensions:

DCTAP extensions in support of ShEx
-----------------------------------

- **`"Extra" properties <https://shex.io/shex-primer/#extra-properties>`_.** In ShEx, once a property is "mentioned" in a triple constraint, that mention "closes the property". As explained in the ShEx Primer: "By default, for an RDF data node to match that shape, every outgoing arc from that node that uses a mentioned predicate must match a triple constrain in the shape". This interpretation coincides with what property mentions are commonly understood to mean in the context of Dublin Core-style application profiles. ShEx also allows a given predicate to be "opened", such that any number of additional arcs using that predicate can be accepted. For example, if shape has two triple constraints that mention the predicate ``rdf:type`` --- one constrained to class A as its value and one constrained to class B, then an outgoing type arc with a value of class C would by default fail validation. However, if that predicate is flagged in the shape as an "extra" property by use of the ShExC keyword ``EXTRA``, the outgoing type arc with a value of class C would pass validation. This behavior of ShEx can be supported by adding ``EXTRA`` as an extension element.

- **`Closed shapes <https://shex.io/shex-primer/#closed-shapes>`_.** In ShEx, shapes are matched against outgoing arcs from a given focus node in terms of the predicates mentioned in the triple constraints, and any other outgoing arcs --- triples that do not have the mentioned properties as their predicates --- are by default simply ignored. However, a given shape can be "closed" (by using the ShExC keyword ``CLOSED``), which means that `all` outgoing arcs from the given focus node must match the given set of triple constraints. In other words, a closed shape will pass validation only if all of its outgoing arcs match `and` there are no other outgoing arcs from that node in the data. This behavior of ShEx can be supported by adding ``CLOSED`` as an extension element for shapes.
- 
