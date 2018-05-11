import pandas as pd
import altair as alt
SRC_PATH = Path('datastash', 'tidied', 'nasa_global_temps.csv')

df = pd.read_csv(SRC_PATH)
chart = alt.Chart(df).mark_line().encode(
            x='year',
            y='temperature_anomaly',
        )

