from pathlib import Path
import csv

# File paths
DATA_PATH = Path('datastash')
DATA_BASENAME = 'nasa_global_temps.csv'
TIDY_PATH = DATA_PATH.joinpath('tidied', DATA_BASENAME)

# meta stuff
METRICS = ['lowess', 'avg']
STAT_FOOS = [max, min]


# opening the data
with open(TIDY_PATH) as i:
    records = []
    for d in csv.DictReader(i):
        d['year'] = int(d['year'])
        d['temperature_anomaly'] = float(d['temperature_anomaly'])
        records.append(d)

# # year with the highest and lowest avg
# subrecs = [r for r in records if r['metric'] == 'avg']
# results['avg'] = xd = {}
# xd['max'] = max(subrecs, key=lambda x: x['temperature_anomaly'])
# xd['min'] = min(subrecs, key=lambda x: x['temperature_anomaly'])


# # year with hi/lo lowess
# subrecs = [r for r in records if r['metric'] == 'lowess']
# results['lowess'] = xd = {}
# xd['max'] = max(subrecs, key=lambda x: x['temperature_anomaly'])
# xd['min'] = min(subrecs, key=lambda x: x['temperature_anomaly'])


results = {}
for metric_name in METRICS:
    subrecs = [r for r in records if r['metric'] == metric_name]
    results[metric_name] = mx = {}
    for foo in STAT_FOOS:
        mx[foo.__name__] = foo(subrecs, key=lambda x: x['temperature_anomaly'])

z = []
for metric_name, x in results.items():
    for agg_name, row in x.items():
        s = [metric_name, agg_name, row['year'], row['temperature_anomaly']]
        z.append(s)

print(z)

