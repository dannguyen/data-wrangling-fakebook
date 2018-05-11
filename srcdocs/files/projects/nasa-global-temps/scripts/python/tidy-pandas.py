import pandas as pd
from pathlib import Path

# File paths
DATA_PATH = Path('datastash')
SRC_PATH = DATA_PATH.joinpath('parsed', 'nasa_global_temps.csv')
DEST_PATH = DATA_PATH.joinpath('tidied', 'nasa_global_temps.csv')
DEST_PATH.parent.mkdir(parents=True, exist_ok=True)

ID_FIELDS = ['year']
VALUE_FIELDS =  ['annual_mean', 'lowess_smoothed']


df = pd.read_csv(SRC_PATH)

t_df = pd.melt(df,
               id_vars=ID_FIELDS,
               var_name=''
               value_vars=VALUE_FIELDS,


