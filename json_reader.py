"""
Script to clean NumPy exercises jupyter notebook from
solutions cells
"""

import json
from typing import final

with open('NumPy  exercises - with solutions.ipynb', 'r') as file:
    data = json.load(file)

cells = data['cells']

for cell in cells:
    if cell['metadata'] == {"cell_type": "solution"}:
        cells.remove(cell)

for cell in cells:
    cell['source'][0].replace(' ', ' ')

final_json = json.dumps(data, indent=4)
with open('Numpy exercises.ipynb', 'w') as file:
    file.write(final_json)

# "metadata": { "cell_type": "solution" }
