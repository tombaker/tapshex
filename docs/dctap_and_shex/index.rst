.. _about_dctap:

DCTAP and ShEx
--------------

The DCTAP model is intended to be usable in a wide range of implementation scenarios, even with technologies not based on RDF. So as not to clash with assumptions underlying such implementations, DCTAP was intentionally defined with the weak semantics. allowing implementers the freedom to define their own interpretations.

The DCTAP model, for example, does not articulate an overly specific view on how shapes relate to data. ShEx, in contrast, does have a strong view. In ShEx, the triple constraints of a shape are evaluated against all of the triples in an RDF graph that touch a given data node (the "focus node"), as determined by a "shape map" that specifies the set of focus nodes either by query or by enumeration. ShEx is also very precise about whether shapes, and their statement constraints, are by default considered "open" or "closed", questions that the DCTAP model deliberately leaves out of scope.

The **tapshex** module supports a subset of ShEx that is expressive enough for the simplest use cases but falls far short of ShEx in its expressivity. One might use DCTAP with ShEx extensions in the following ways:

- If the subset of ShEx features is sufficient, one might use DCTAP as an alternative to the standard syntaxes for ShEx --- the compact syntax (ShExC), JSON syntax (ShExJ), and the less frequently used RDF syntax (ShExR). 
- DCTAP can serve as an on-ramp to ShEx itself, and specifically to the ShExC syntax --- a starter syntax for users new to ShEx who may find the spreadsheet format more approachable or easier to grok than the Turtle-like ShExC syntax, where users need not know where ShExC expects curly, pointy, or square brackets, semi-colons, or at-signs, or in what order node and cardinality constraints are placed in a triple constraint. 
- DCTAP can serve as a tool for learning ShExC syntax. 
- One might use DCTAP for rapidly prototyping ShEx schemas, then gradually leave DCTAP behind and continue on with the more expressive ShEx. 

As discussed in the pages below, the choice between DCTAP and ShEx may be determined by specific requirements for expressivity.
