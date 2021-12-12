import pandas as pd
 
# Read data
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_nc.csv',sep=',')

# Subset
df = df[df['artist'] == 'ArianaGrandeVevo']
print(df['artist'])

# There's 108 rows left in the dataframe
