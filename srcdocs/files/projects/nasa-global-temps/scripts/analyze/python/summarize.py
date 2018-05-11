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



# lowess: stdev, max, min, sum, mean, median
# avg: stdev, max, min, sum, mean, median
