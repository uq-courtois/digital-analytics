import pandas as pd
 
# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube_vevo.csv',sep=',')

# Create variable year from published (extract the last four characters)
df['year'] = df['published'].str[-4:]
df['year'] = df['year'].astype('int')
