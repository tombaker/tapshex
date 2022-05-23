.. _node_type_nonliteral:

Node type: NONLITERAL
.....................

The **dctap** module supports, by default, keywords for the three types of node as defined in the RDF model: `IRI, BNODE, and LITERAL <https://dctap-python.readthedocs.io/en/latest/elements/valueNodeType/index.html#>`_.

Like ShEx, **tap2shex** supports, in addition, the keyword NONLITERAL, as an alias for "IRI or BNODE".

In both **dctap** and **tap2shex**, keywords are case-insensitive, with the difference that in **dctap**, they are normalized to lowercase and in **tap2shex** to uppercase.
