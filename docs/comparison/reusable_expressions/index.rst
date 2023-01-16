.. _reusable_expressions:

Reusable expressions
....................

`In a ShEx schema <https://shex.io/shex-primer/#labeled-constraints>`_, one can assign a name to a frequently used set of node constraints (eg, to say: "integer between 1970 and 2022", then reference that name in the context of multiple triple constraints. A triple expression can also be defined and labeled just once, then referenced in multiple shapes (eg, if the subjects of "user" and "employee" shapes are both expected to have names and email addresses).

In a DCTAP instance, constraints are repeated in every statement template to which they apply, and statement templates are repeated in every shape to which they apply. In other words, a ShEx schema can be `"DRY" <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, while DCTAP instances are "WET" ("Write Every Time"). Of course, DCTAP can serve as a stepping stone to ShEx, where a wet schema, once generated, can be dried.
