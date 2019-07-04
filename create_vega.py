import csv
import json
from datetime import datetime
from pathlib import Path


def to_float(v, default=0):
    try:
        return float(v)
    except ValueError:
        return default


data = []
with Path('summaries.txt').open(newline='', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # if row['autoParallel'].lower() == 'no':
        data.append({
            'date': datetime.strptime(row['hwAvail'], '%b-%Y').strftime('%Y-%m'),
            'mhz': float(row['mhz']),
            'peak': to_float(row['peak']),
            'base': to_float(row['base']),
        })

print(f'included: {len(data)}')

# with Path('simple.csv').open('w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
#
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)
Path('charts/data.json').write_text(json.dumps(data))
