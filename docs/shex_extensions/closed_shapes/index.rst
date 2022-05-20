.. _closed_shapes:

CLOSED 
......

In ShEx, shapes are matched against outgoing arcs from a given focus node in terms of the predicates mentioned in the triple constraints, and any other outgoing arcs --- triples that do not have the mentioned properties as their predicates --- are by default simply ignored. However, a given shape can be "closed" (by using the ShExC keyword ``CLOSED``), which means that `all` outgoing arcs from the given focus node must match the given set of triple constraints. 

In other words, a `closed shape <https://shex.io/shex-primer/#closed-shapes>`_ will pass validation only if all of its outgoing arcs match `and` there are no other outgoing arcs from that node in the data.
- 
