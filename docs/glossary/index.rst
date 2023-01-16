.. _model_glossary:

ShEx Glossary
-------------

This glossary defines terms that are specific to ShEx; definitions in double quotes are taken verbatim from the `Shape Expressions Primer <https://shexspec.github.io/primer/>`_. See the :doc:`DCTAP Glossary <dctap:glossary/index>` for definitions of
**Application Profile**,
**Blank Node**,
**Compact IRI**,
**CSV File**,
**Datatype**,
**DCTAP Element**,
**DCTAP CSV File**,
**Description**,
**Entity**,
**Instance Data**,
**IRI**,
**Language Tag**,
**Literal**,
**Property**,
**Predicate Constraint**,
**Shape**,
**Statement**,
**Statement Template**,
**URI**,
**Value**,
**Value Constraint**, and
**Vocabulary**.

.. glossary::

   Constraint
       "A restriction on the set of permissible nodes or triples."

   Focus Node
       "An RDF data node of interest that is examined during validation."

   Shape Map
       "A collection of pairs of RDF data nodes and ShEx shapes that is used for invoking validation and reporting results."

   Shape (ShEx)
       "A triple expression against which a focus node is tested to see whether all incoming or outgoing arcs, which match predicates in the triple expression, have the appropriate cardinality and values."

   ShExC
       "A compact syntax meant for human eyes and fingers."

   ShExJ
       "A JSON-LD representation meant for machine processing."

   ShExR
       "The RDF interpretation of ShExJ expressible in any RDF syntax."

   ShEx Schema
       "A collection of shape expressions."

   Triple Constraint
       "A constraint with a given predicate which is tested against RDF triples with that predicate and the focus node as subject (or object, for Inverse Triple Constraints)."

   Triple Expression
       "A collection of triple constraints which may be combined in groups or choices."

   Value (ShEx)
       "A shorthand designation for the RDF node at the opposite end of an RDF data type from a focus node. In typical usage, this is the object of a triple or, for inverse triple constraints, its subject."
