import pandas as pd
 
# Read file
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv',sep=',') 
 
# Calculate the median views per artist
grouped = df.groupby(['artist'], as_index=False)[['like']].mean()
 
# Print artist and views variables
print(grouped[['artist','like']])
