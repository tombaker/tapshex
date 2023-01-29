@Nishad - I have made alot of progress with tapshex and am working on unit
tests. For each example in the ShEx primer that is supported by DCTAP, in terms
of features, I am creating a TAP, then the unit tests convert it first into a
Python dictionary and then, using the Jinja template, into ShExC. I am stuck on
two features of Jinja and would really appreciate if you could tweak template.
Specifically:

The template is at: https://github.com/tombaker/tapshex/blob/main/tapshex/template.py

The features not yet supported are:
- valueConstraintType 'picklist': https://github.com/tombaker/tapshex/blob/main/tests_primer/nishad/test_csv_to_dict.py#L44-L45
- Value shape: https://github.com/tombaker/tapshex/blob/main/tests_primer/nishad/test_csv_to_dict.py#L48
- "At least one statement" (ie, `IRI+`) - https://github.com/tombaker/tapshex/blob/main/tests_primer/nishad/test_csv_to_dict.py#L60
  - I find this syntax confusing because the `+` sign refers to the cardinality of the statement, not of the node type `IRI`.
  - Would it perhaps be easier to use the regular syntax for cardinality - ie, `{1,}`?

The result should look like: 
- https://github.com/tombaker/tapshex/blob/main/tests_primer/nishad/primer.shexc#L7-L13
