from jinja2 import Template
from pyshexc.parser_impl.generate_shexj import parse
import json

tap = """
shapeID,propertyID,valueNodeType,valueDataType,minoccurs,maxoccurs,mininclusive,maxinclusive
school:Enrollee,ex:hasGuardian,iri,,1,2
,foaf:age,,xsd:integer,,,13,20
"""

ap_dict = {
	"namespaces": {
		"ex": "http://ex.example/#",
		"xsd": "http://www.w3.org/2001/XMLSchema#",
		"school": "http://school.example/#",
		"foaf": "http://xmlns.com/foaf/0.1/"
	},
	"shapes": [
		{
			"shapeID": "school:Enrollee",
			"statement_templates": [
				{
					"propertyID": "ex:hasGuardian",
					"valueNodeType": "iri",
					"min": "1",
					"max": "2",
				},
				{
					"propertyID": "foaf:age",
					"valueDataType": "xsd:integer",
					"MinInclusive": "13",
					"MaxInclusive": "20",
				}
			]
		}
	]
}

shex_jinja = """
{%- for prefix, uri in namespaces.items() %}
PREFIX {{prefix}}: <{{uri}}>
{%- endfor %}

{%- for shape in shapes %}
{{shape.shapeID}} {
  {%- for statement in shape. statement_templates %}
  {{statement.property}} {{statement.propertyID}} 
  {%- if statement.valueNodeType %} {{statement.valueNodeType|upper}}{% endif -%}
  {%- if statement.valueDataType %} {{statement.valueDataType}}{% endif -%}
  {%- if statement.minoccurs or statement.maxoccurs %} { {{-statement.minoccurs-}}
		{%- if statement.maxoccurs -%}
		 ,{{statement.maxoccurs}} 
		{%- endif -%} }
  {%- endif -%}
  {%- if statement.MaxInclusive %} MaxInclusive {{statement.MaxInclusive}} {%- endif -%}
  {%- if statement.MinInclusive %} MinInclusive {{statement.MinInclusive}} {%- endif -%}
  {%- if not loop.last -%} ;{%- endif -%}
  {%- endfor %}
}
{%- endfor %}
"""

template = Template(shex_jinja)
shexc_output = template.render(ap_dict)

json_ap=parse(shexc_output)._as_json
parsed = json.loads(json_ap)

from pprint import pprint
for line in shexc_output.splitlines():
    print(line)

# pprint(shexc_output)

# pprint(json_ap)
