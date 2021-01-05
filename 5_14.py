import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
# Sum the views per artist
grouped = df.groupby(['artist'], as_index=False)[['views']].sum() 
 
# Print artist and views variables
print(grouped[['artist','views']])
