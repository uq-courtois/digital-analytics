import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
# Calculate the median views per artist
grouped = df.groupby(['artist'], as_index=False)[['views']].median()
 
# Print artist and views variables
print(grouped[['artist','views']])
