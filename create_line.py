import csv
import json
from datetime import datetime
from operator import itemgetter
from pathlib import Path
from statistics import mean


def to_float(v, default=0):
    try:
        return float(v)
    except ValueError:
        return default


epoch = datetime(1970, 1, 1)


def to_s(y):
    return int((datetime(y, 6, 1) - epoch).total_seconds() * 1000)


data = {}
with Path('summaries.txt').open(newline='', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # if row['autoParallel'].lower() == 'no':
        date = datetime.strptime(row['hwAvail'], '%b-%Y').year
        speed = float(row['mhz']) / 1000
        if date in data:
            data[date].append(speed)
        else:
            data[date] = [speed]


data = sorted([{'date': to_s(k), 'speed': mean(v)} for k, v in data.items()], key=itemgetter('date'))
print('points:', len(data))
Path('charts/line-data.json').write_text(json.dumps(data, indent=2))
