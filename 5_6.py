import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo_dp.csv',sep=';') 

# Shape of df
print(df.shape)

# Counting duplicate rows
print(df.duplicated().sum())

# Showing rows with duplicates
print(df[df.duplicated()])

# Drop exact duplicates
df = df.drop_duplicates() 

# Shape of df
print(df.shape)
