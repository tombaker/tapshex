"""Default settings."""

DEFAULT_CONFIGFILE_NAME = "tapshex.yml"
DEFAULT_HIDDEN_CONFIGFILE_NAME = ".tapshexrc"
DEFAULT_CONFIG_YAML = """# tapshex config file (YAML format)

# See https://tapshex.readthedocs.io/en/latest/config/
# for advanced configuration options

prefixes:
    ":":        "http://example.org/"
    "dc:":      "http://purl.org/dc/elements/1.1/"
    "dcterms:": "http://purl.org/dc/terms/"
    "dct:":     "http://purl.org/dc/terms/"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "owl:":     "http://www.w3.org/2002/07/owl#"
    "rdf:":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    "rdfs:":    "http://www.w3.org/2000/01/rdf-schema#"
    "schema:":  "http://schema.org/"
    "skos:":    "http://www.w3.org/2004/02/skos/core#"
    "skosxl:":  "http://www.w3.org/2008/05/skos-xl#"
    "wdt:":     "http://www.wikidata.org/prop/direct/"
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"

extra_value_node_types:
- nonliteral

element_aliases:
    "mand": "mandatory"
    "rep": "repeatable"
"""
