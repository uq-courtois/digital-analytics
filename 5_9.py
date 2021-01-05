import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Print df info to get a variable overview
print(df.info())

# Categorise in (1) Equal or larger than 1000000 views or (0) lower than 1000000 views
df['cutoff'] = df['views'].apply(lambda x: 1 if x >= 1000000 else 0)

# Check new variable cutoff alongside views variable
print(df[['views','cutoff']])
