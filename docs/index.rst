.. _home:

tap2shex
========

**tap2shex** is a module and command-line utility for reading and interpreting spreadsheet (CSV) files formatted according to the `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ and expressing them as schemas in the `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_.

This module imports and builds on `dctap <https://github.com/dcmi/dctap-python>`_, a module and command-line utility for parsing CSVs, performing some very basic consistency checks, and emitting normalized representations of given CSV contents in plain text, YAML, or JSON. The features and behavior of **dctap** are extensively documented `on dctap-python.readthedocs.io <https://dctap-python.readthedocs.io/en/>`_.

This module does not replicate the command-line interface or documentation of **dctap**. Rather, it relies on **dctap** for basic features (and their documentation) and extends **dctap** with a complementary set of features that are explicitly aligned with ShEx. 

So as to be usable in a wide range of implementation scenarios, even with technologies not based on RDF, the DCTAP model was designed with intentionally weak semantics. The DCTAP model does not itself articulate strong positions on the nature of shapes so as to allow implementers the freedom to define their own interpretations. In ShEx, for example, the triple constraints of a shape are evaluated against all of the triples in an RDF graph that touch a given data node (the "focus node"), as determined by a "shape map" that specifies the set of focus nodes either by query or by enumeration. DCTAP, in contrast, leaves such specifics to implementers. Where ShEx is very precise about whether shapes, and their statement constraints, are by default considered "open" or "closed", the DCTAP model deliberately leaves such questions out of scope.

The following pages compare DCTAP and ShEx in terms of expressivity, document various extensions to the DCTAP model in support of ShEx, and clarify how a DCTAP instance is to be interpreted in terms of ShEx.

DCTAP plus ShEx extensions is expressive enough for simple use cases. Inasmuch as **tap2shex** supports a subset of ShEx, one might use it as an alternative to the standard, full-featured syntaxes for ShEx --- the compact syntax (ShExC), JSON syntax (ShExJ), and the less frequently used RDF syntax (ShExR). Or one might consider DCTAP as an on-ramp to ShEx itself, and specifically to the ShExC syntax --- a starter syntax for users new to ShEx who may find the spreadsheet format more approachable or easier to grok than the Turtle-like ShExC syntax. Or one might use the DCTAP format for rapidly prototyping a ShEx schema, then leave DCTAP behind and continue on with ShExC. The choices may be determined by specific requirements for expressivity, as discussed in the pages below.

This module is under development at `https://github.com/tombaker/tap2shex <https://github.com/tombaker/tap2shex>`_, and issues or questions can be posted there in its `issue tracker <https://github.com/tombaker/tap2shex>`_.

.. toctree::
   :maxdepth: 6

   dctap_and_csv/index
   dctap_and_shex/index
   shex_extensions/index
   glossary/index

