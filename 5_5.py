import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Subsetting dataframe
subset = df[df['views'] > 1000000]

# Printing info of subset
print(subset.info()) # Should be 3615 records
