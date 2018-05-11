import pandas as pd
from pathlib import Path

# File paths
DATA_PATH = Path('datastash')
DATA_BASENAME = 'nasa_global_temps.csv'
SRC_PATH = DATA_PATH.joinpath('parsed', DATA_BASENAME)
DEST_PATH = DATA_PATH.joinpath('tidied', DATA_BASENAME)
DEST_PATH.parent.mkdir(parents=True, exist_ok=True)

# metadata
ID_FIELDS = ['year']
VALUE_FIELDS =  ['avg', 'lowess']

# read from file
df = pd.read_csv(SRC_PATH)

# melt data, then sort it
t_df = pd.melt(df, id_vars=ID_FIELDS,
                   var_name='metric',
                   value_vars=VALUE_FIELDS,
                   value_name='temperature_anomaly',
       ).sort_values(by=['year', 'metric'], ascending=[True, True])

# write to disk
t_df.to_csv(DEST_PATH, index=False)
