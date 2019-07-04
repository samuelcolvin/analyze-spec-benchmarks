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
        if 'int' in row['benchType'].lower():
            data.append({
                'date': datetime.strptime(row['hwAvail'], '%b-%Y').strftime('%Y-%m'),
                'speed': float(row['mhz']) / 1000,
            })

print('points:', len(data))
Path('charts/scatter-data.json').write_text(json.dumps(data))
