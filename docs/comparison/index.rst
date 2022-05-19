.. _comparison:

DCTAP and ShEx compared
-----------------------

The `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ was designed to fit within the limitations of the Common Format and MIME Type for Comma-Separated Values (CSV) Files, `RFC 4018 (2005) <https://tools.ietf.org/html/rfc4180>`_. This format consists of exactly one two-dimensional grid of rows and columns. 

Modern spreadsheet programs, such as Excel and Google Sheets, support multiple grids in separate tabs, and they support hyperlinks between tabs --- features which allow the construction of tabular databases. However, spreadsheets more complex than one single, two-dimensional grid only work with file formats that are specific to a given application.

DCTAP was therefore designed with a base model that adheres to the limitations of RFC 4180, and the expressivity of DCTAP as a language for application profiles is limited to things that can readily be encoded in two dimensions. The designers of DCTAP recognized that creators of application profiles might want to extend the limits of that expressivity but were also keen to avoid making DCTAP overly complex. The **dctap** module was designed with various extension points for activating support for additional elements. The nature and interpretation of such extensions, in general, is beyond the scope of DCTAP itself. This module, **tap2shex**, constitutes an extension of DCTAP for use with ShEx.

The `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_ is not bound by the limitations of two dimensions. It is a sophisticated language for describing RDF graph structures, with a well-defined grammar. ShEx supports the expression of constructs that would be difficult or impossible to express in a simple CSV:

- 
