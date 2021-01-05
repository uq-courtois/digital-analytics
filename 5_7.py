import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo_dp.csv',sep=';') 

# Shape of df
print(df.shape)

# Print missing data count
print(df.isnull().sum()) 

# Print rows with missing data
isolatemissing = pd.isnull(df['views'])
print(df[isolatemissing])

# Drop duplicates
df = df.dropna()

# Shape of df
print(df.shape)
