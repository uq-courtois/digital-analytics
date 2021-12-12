import pandas as pd
 
# Read data
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_nc.csv',sep=',')

# For an overview
print(df['artist'].unique())

# To have the number of unique values, wrap in len()
# Answer: 197 unique artists
print(len(df['artist'].unique()))
