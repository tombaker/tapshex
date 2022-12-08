.. _home:

About tapshex
=============

**tapshex** is a package and command-line utility for reading and interpreting :dctap:term:`CSV File`\s formatted according to the :doc:`dctap:model/index` and expressing them as schemas in the `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_. This package imports classes and functions from a related package, `**dctap** (see <https://dctap-python.readthedocs.io/en/latest/index.html>`_), and extends them for use with ShEx. 

**tapshex** provides a command-line tool that is almost identical its counterpart in **dctap** but with added support for generating ShEx schemas.

This documentation extensively links to, and builds on, the documentation for **dctap**.

A module and command-line utility for parsing CSVs, performing some very basic consistency checks, and emitting normalized representations of given DCTAP instance in plain text, YAML, or JSON. The features and behavior of **dctap** are extensively documented `on dctap-python.readthedocs.io <https://dctap-python.readthedocs.io/en/>`_.

This module does not replicate the command-line interface or documentation of **dctap**. Rather, it relies on **dctap** for basic features (and their documentation) and extends **dctap** with a complementary set of features that are explicitly aligned with ShEx. 

These documentation pages compare DCTAP and ShEx in terms of expressivity, document various extensions to the DCTAP model in support of ShEx, and clarify how a DCTAP instance is to be interpreted in terms of ShEx. This discussion assumes familiarity with the basics of ShEx, and of its terminology, as described in the `ShEx Primer <https://shexspec.github.io/primer/>`_.

This module is under development at `https://github.com/tombaker/tapshex <https://github.com/tombaker/tapshex>`_. Issues or questions about **tapshex** can be posted in its `issue tracker <https://github.com/tombaker/tapshex>`_.

DCTAP:

- :doc:`dctap:about/index`
- :doc:`dctap:cli/index`
- :doc:`dctap:cli/installation/index`
- :doc:`dctap:cli/subcommands/index`
- :doc:`dctap:cli/subcommands/init/index`
- :doc:`dctap:cli/subcommands/read/index`
- :doc:`dctap:config/index`
  - :doc:`dctap:config/default_shape_name/index`
  - :doc:`dctap:config/element_aliases/index`
  - :doc:`dctap:config/extra_elements/extra_shape_elements/index`
  - :doc:`dctap:config/extra_elements/extra_statement_template_elements/index`
  - :doc:`dctap:config/extra_elements/index`
  - :doc:`dctap:config/list_elements/index`
  - :doc:`dctap:config/list_elements/valueNodeType/index`
  - :doc:`dctap:config/list_item_separator/index`
  - :doc:`dctap:config/prefix_mappings/index`
- :doc:`dctap:design/element_names/index`
- :doc:`dctap:design/elements_not_repeatable/index`
- :doc:`dctap:design/elements_reordered/index`
- :doc:`dctap:design/elements_repurposed/index`
- :doc:`dctap:design/elements_unknown_ignored/index`
- :doc:`dctap:design/empty_rows_ignored/index`
- :doc:`dctap:design/index`
- :doc:`dctap:design/keywords_lowercased/index`
- :doc:`dctap:design/reserved_names/index`
- :doc:`dctap:design/shapes_declared_once/index`
- :doc:`dctap:design/shapes_on_own_rows/index`
- :doc:`dctap:elements/index`
- :doc:`dctap:elements/mandrepeat/index`
- :doc:`dctap:elements/note/index`
- :doc:`dctap:elements/propertyID/index`
- :doc:`dctap:elements/shapeID/index`
- :doc:`dctap:elements/valueConstraintType/IRIStem/index`
- :doc:`dctap:elements/valueConstraintType/LanguageTag/index`
- :doc:`dctap:elements/valueConstraintType/MinInclusive_MaxInclusive/index`
- :doc:`dctap:elements/valueConstraintType/MinLength_MaxLength/index`
- :doc:`dctap:elements/valueConstraintType/Pattern/index`
- :doc:`dctap:elements/valueConstraintType/Picklist/index`
- :doc:`dctap:elements/valueConstraintType/index`
- :doc:`dctap:elements/valueConstraintType/value_constraint_no_type/index`
- :doc:`dctap:elements/valueConstraintType/value_constraint_type_no_constraint/index`
- :doc:`dctap:elements/valueConstraintType/value_constraint_types_builtin/index`
- :doc:`dctap:elements/valueConstraintType/value_constraint_types_custom/index`
- :doc:`dctap:elements/valueDataType/index`
- :doc:`dctap:elements/valueNodeType/index`
- :doc:`dctap:elements/valueShape/index`
- :doc:`dctap:glossary/index`
- :doc:`dctap:index`
- :doc:`dctap:model/index`
- :doc:`dctap:model/minimum_profile/index`

.. toctree::
   :maxdepth: 6

   dctap_and_csv/index.rst
   dctap_and_shex/index.rst
   comparison/index.rst
   extensions/index.rst
   glossary/index.rst

