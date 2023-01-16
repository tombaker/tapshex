.. _comparison:

ShEx features not supported by DCTAP
------------------------------------

The `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_ is a sophisticated language for describing RDF graph structures, with a well-defined grammar and a level of expressivity beyond what is attainable in a two-dimensional table.

Many ShEx features are not supported in the base DCTAP model, notably:

.. toctree::
   :maxdepth: 2

   reusable_expressions/index.rst
   combinations/index.rst
   nested_shapes/index.rst
   inverse_triple_constraints/index.rst
   negative_triple_constraints/index.rst
   imported_schemas/index.rst

Other features in the pipeline for the next release of the ShEx semantics include:

- **inheritance**: defining a shape expression as an extension or restriction of another shape
- **abstract shapes**: flagging a shape such that only shapes inheriting from that shape may satisfy the shape (analogously to object-oriented programming, where abstract classes may not be instantiated, only used for deriving non-abstract classes)
