.. _home:

tap2shex
========

**tap2shex** is a module and command-line utility for reading and interpreting spreadsheet (CSV) files formatted according to the `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ and expressing them as schemas in the `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_.

This module imports and builds on `dctap <https://github.com/dcmi/dctap-python>`_, a module and command-line utility for parsing CSVs, performing some very basic consistency checks, and emitting normalized representations of given DCTAP instance in plain text, YAML, or JSON. The features and behavior of **dctap** are extensively documented `on dctap-python.readthedocs.io <https://dctap-python.readthedocs.io/en/>`_.

This module does not replicate the command-line interface or documentation of **dctap**. Rather, it relies on **dctap** for basic features (and their documentation) and extends **dctap** with a complementary set of features that are explicitly aligned with ShEx. 

These documentation pages compare DCTAP and ShEx in terms of expressivity, document various extensions to the DCTAP model in support of ShEx, and clarify how a DCTAP instance is to be interpreted in terms of ShEx. This discussion assumes familiarity with the basics of ShEx, and of its terminology, as described in the `ShEx Primer <https://shexspec.github.io/primer/>`_.

This module is under development at `https://github.com/tombaker/tap2shex <https://github.com/tombaker/tap2shex>`_. Issues or questions about **tap2shex** can be posted in its `issue tracker <https://github.com/tombaker/tap2shex>`_.

.. toctree::
   :maxdepth: 6

   dctap_and_csv/index.rst
   dctap_and_shex/index.rst
   comparison/index.rst
   extensions/index.rst
   glossary/index.rst

