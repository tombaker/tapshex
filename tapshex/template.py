"""Jinja template."""


SHEX_JINJA = """
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
