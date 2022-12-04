.. _dctap_and_csv:

DCTAP and CSV
-------------

The `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ adheres to `RFC 4108 <https://tools.ietf.org/html/rfc4180>`_, the Common Format and MIME Type for Comma-Separated Values (CSV) Files. The CSV format consists of exactly one two-dimensional grid of rows and columns, so DCTAP is limited to things that can readily be encoded in two dimensions.

Modern spreadsheet programs, such as Excel and Google Sheets, transcend these limitations by supporting multiple grids in separate tabs, with hyperlinks across tabs --- features which support drop-down menus and the construction of simple tabular databases --- though at the cost of using non-standard file formats. Implementations of DCTAP in the wild have already leveraged such features to good effect, as "extensions" to DCTAP, but for **tapshex**, such extensions are out of scope.

As implemented in **dctap-python**, the base DCTAP model can be extended for use with extra elements defined specifically to support `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_.
