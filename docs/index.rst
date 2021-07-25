tap2shex
========

**tap2shex** is a module and command-line utility for reading and interpreting CSV files formatted according to the `DC Tabular Application Profiles (DCTAP) model <https://github.com/dcmi/dctap/blob/main/TAPprimer.md>`_ and expressing them as ShEx schemas. The module is being developed at `https://github.com/tombaker/tap2shex <https://github.com/tombaker/tap2shex>`_.

**tap2shex** imports and builds on `**dctap** <https://github.com/dcmi/dctap-python>`_, a module for reading a CSV formatted according to the `DCTAP Model <https://dctap-python.readthedocs.io/en/latest/model/index.html>`_, using its columns to define `Statement Constraints <https://dctap-python.readthedocs.io/en/latest/glossary/index.html#term-Statement-Constraint>`_ and group these under `Shapes <https://dctap-python.readthedocs.io/en/latest/glossary/index.html#term-Shape>`_. In so doing, it normalizes CSV headers (by supporting aliases and tolerating whitespace, dashes, and underscores) and values (eg, "1" is "true"), optionally expands namespace prefixes, and issues warnings to stderr about inconsistencies (eg, when a node type of IRI is used in combination with an RDF datatype). **Dctap** outputs the result to stdout as text, JSON, or YAML. This is all described pretty thoroughly on Readthedocs [3].

**tap2shex** replicates the command-line interface and configuration file options of **dctap**, with minor differences and extensions that are specific to ShEx.
