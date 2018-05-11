from csv import writer as csvwriter
from pathlib import Path
from re import compile as rxcompile

# File paths
DATA_PATH = Path('datastash')
SRC_PATH = DATA_PATH.joinpath('originals', '647_Global_Temperature_Data_File.txt')
DEST_PATH = DATA_PATH.joinpath('parsed', 'nasa_global_temps.csv')
DEST_PATH.parent.mkdir(parents=True, exist_ok=True)

# parsing meta info
FIELD_NAMES = ['year',
               'avg',
               'lowess',]

FIELD_PATTERN = rxcompile(
                    r'(^\d{4})'
                    r'\s+'
                    r'(.+?)'
                    r'\s+'
                    r'(.+)$')


with open(DEST_PATH, 'w') as _d:
    dest = csvwriter(_d)
    dest.writerow(FIELD_NAMES)

    with open(SRC_PATH, 'r') as src:
        for line in src:
            m = FIELD_PATTERN.match(line)
            if m:
                dest.writerow(m.groups())

