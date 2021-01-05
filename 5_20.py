import pandas as pd
 
# Read file
df = pd.read_csv('mtv-artists_genres.csv',sep=',') 

# Generate dataframe with counts per genre
x = df.groupby(['genre'], as_index=False)[['mtv']].count()
x = x.rename(columns={"mtv": "count"})

print(x)
