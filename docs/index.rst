.. _home:

tap2shex
========

**tap2shex** is a module and command-line utility for reading and interpreting spreadsheet (CSV) files formatted according to the `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ and expressing them as schemas in the `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_.

**tap2shex** imports and builds on `dctap <https://github.com/dcmi/dctap-python>`_, a module and command-line utility for parsing CSVs, performing some very basic consistency checks, and emitting normalized representations of given CSV contents in plain text, YAML, or JSON. The features and behavior of **dctap** are extensively documented `on dctap-python.readthedocs.io <https://dctap-python.readthedocs.io/en/>`_.

**tap2shex** does not replicate the command-line interface or documentation of **dctap**. Rather, it supports an extended and complementary set of features that are explicitly aligned with ShEx. These documentation pages, `at tap2shex.readthedocs.io <https://tap2shex.readthedocs.io/en/>`_, focus on comparing DCTAP and ShEx in terms of expressivity and on documenting features and extensions that are specific to ShEx.


The module is being developed at `https://github.com/tombaker/tap2shex <https://github.com/tombaker/tap2shex>`_, issues or questions can be posted in an `issue tracker <https://github.com/tombaker/tap2shex>`_.

.. toctree::
   :maxdepth: 6

   comparison/index
   glossary/index

