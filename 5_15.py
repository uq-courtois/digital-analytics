import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
# Standard deviation of likes per artist
grouped = df.groupby(['artist'], as_index=False)[['like']].std()
 
# Print artist and views variables
print(grouped[['artist','like']])
