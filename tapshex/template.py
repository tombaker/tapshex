"""Jinja template."""


SHEX_JINJA = """
{%- for prefix, uri in namespaces.items() %}
PREFIX {{prefix}} <{{uri}}>
{%- endfor %}

{%- for shape in shapes %}
{{shape.shapeID}} {
  {%- for statement in shape.statement_templates %}
  {{statement.propertyID}}
  {%- if statement.valueNodeType %} {{statement.valueNodeType|upper}}{% endif -%}
  {%- if statement.valueDataType %} {{statement.valueDataType}}{% endif -%}
  {%- if statement.valueShape %} @{{statement.valueShape}}{% endif -%}
  {%- if statement.valueConstraint is defined -%} 
        {%- if statement.valueConstraintType == 'picklist_quoted' -%}
            {{" "}}[{{ statement.valueConstraint | map('tojson') | join(" ") }}]
        {%- elif statement.valueConstraintType == "picklist" -%}
            {{" "}}[{{ statement.valueConstraint | join(" ") }}]
        {%- endif -%}
  {%- endif -%}
  {%- if statement.minoccurs or statement.maxoccurs %} { {{-statement.minoccurs-}}
		{%- if statement.maxoccurs -%}
		 ,{{statement.maxoccurs}}
		{%- endif -%} }
  {%- endif -%}
  {%- if statement.mininclusive %} MinInclusive {{statement.mininclusive}} {%- endif -%}
  {%- if statement.maxinclusive %} MaxInclusive {{statement.maxinclusive}} {%- endif -%}
  {%- if not loop.last -%} ;{%- endif -%}
  {%- endfor %}
}
{%- endfor %}
"""
#            {%- elif statement.valueDataType == 'xsd:integer' or statement.valueDataType == "http://www.w3.org/2001/XMLSchema#integer " -%}
#                {{" "}}[{{ statement.valueConstraint | join(" ") }}]
