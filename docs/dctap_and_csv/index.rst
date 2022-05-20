.. _dctap_and_csv:

DCTAP and the CSV tabular format
--------------------------------

The `DC Tabular Application Profiles (DCTAP) model <https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/>`_ adheres to the limitations of the Common Format and MIME Type for Comma-Separated Values (CSV) Files, `RFC 4108 (2005) <https://tools.ietf.org/html/rfc4180>`_. The CSV format consists of exactly one two-dimensional grid of rows and columns, so DCTAP is limited to things that can readily be encoded in two dimensions.

Modern spreadsheet programs, such as Excel and Google Sheets, transcend these limitations by supporting multiple grids in separate tabs, with hyperlinks across tabs --- features which allow the construction of simple tabular databases --- though at the cost of using non-standard file formats.

As implemented in **dctap-python**, the base DCTAP model can be extended for use with extra elements. This module, **tap2shex**, extends DCTAP specifically for use with the `Shape Expressions language (ShEx) <https://shexspec.github.io/primer/>`_.
