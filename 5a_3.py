import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/artists-spotify.csv',delimiter=',')

# Subsetting rows with values for popularity higher than 80
df_pop = df[df['popularity'] > 80]

# 12 out of 81 entries are written into the dataframe df_pop
print(df_pop.info())
