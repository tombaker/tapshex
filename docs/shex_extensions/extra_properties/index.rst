.. _extra_properties:

Shape element: EXTRA
....................

`In ShEx, <https://shex.io/shex-primer/#extra-properties>`_, once a property is "mentioned" in a triple constraint, that mention "closes the property". As explained in the ShEx Primer: "By default, for an RDF data node to match that shape, every outgoing arc from that node that uses a mentioned predicate must match a triple constrain in the shape". 

This interpretation coincides with what "property mentions" are commonly understood to mean in the context of Dublin Core-style application profiles. 

ShEx also allows a given predicate to be "opened", such that any number of additional arcs using that predicate can be accepted. For example, if shape has two triple constraints that mention the predicate ``rdf:type`` --- one constrained to class A as its value and one constrained to class B, then an outgoing type arc with a value of class C would by default fail validation. However, if that predicate is flagged in the shape as an "extra" property by use of the ShExC keyword ``EXTRA``, the outgoing type arc with a value of class C would pass validation. This behavior of ShEx can be supported by adding ``EXTRA`` as an extension element.

