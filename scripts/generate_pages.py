# scripts/generate_pages.py

import yaml
from jinja2 import Environment, FileSystemLoader

# Laad YAML-schema
with open('schemas/pages/home.yaml') as f:
    page_data = yaml.safe_load(f)

# Laad sjablonen
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('page_template.html')

# Render de pagina
output = template.render(page_data)

# Schrijf naar bestand
with open('output/home.html', 'w') as f:
    f.write(output)
