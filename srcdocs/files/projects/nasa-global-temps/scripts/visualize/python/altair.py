import pandas as pd
import altair as alt

# File paths
SRC_PATH = Path('datastash', 'tidied', 'nasa_global_temps.csv')

df = pd.read_csv(SRC_PATH)
