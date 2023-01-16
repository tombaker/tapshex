.. _elements:

DCTAP Elements
^^^^^^^^^^^^^^

In the DCTAP Model, a Shape groups a set of Statement Templates, each of which describes one type of Statement in Instance Data about a specified Entity. Each of these two components (Shapes and Statement Templates) has its own (extensible) set of DCTAP Elements:

Statement Constraint Elements
"""""""""""""""""""""""""""""

Removed from this section:

- :doc:`dctap:elements/mandrepeat/index`
- :doc:`dctap:elements/valueConstraintType/MinInclusive_MaxInclusive/index`
- :doc:`dctap:elements/valueConstraintType/MinLength_MaxLength/index`

This section:

- :doc:`dctap:elements/propertyID/index`
- :doc:`dctap:elements/valueNodeType/index`
- :doc:`dctap:elements/valueDataType/index`
- :doc:`dctap:elements/valueConstraintType/index`

  - :doc:`dctap:elements/valueConstraintType/value_constraint_no_type/index`
  - :doc:`dctap:elements/valueConstraintType/value_constraint_type_no_constraint/index`
  - :doc:`dctap:elements/valueConstraintType/value_constraint_types_builtin/index`

    - :doc:`dctap:elements/valueConstraintType/Picklist/index`
    - :doc:`dctap:elements/valueConstraintType/Pattern/index`
    - :doc:`dctap:elements/valueConstraintType/IRIStem/index`
    - :doc:`dctap:elements/valueConstraintType/LanguageTag/index`

  - :doc:`dctap:elements/valueConstraintType/value_constraint_types_custom/index`

- :doc:`dctap:elements/valueShape/index`
- :doc:`dctap:elements/note/index`

Shape Elements
""""""""""""""

There are two Shape elements. If the shapeID element is not used in a given DCTAP instance, it will be assigned a default value (which can be customized in the config file - see :ref:`default_shape_name`).

- :doc:`dctap:elements/shapeID/index`
