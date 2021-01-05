import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Print df info to get a variable overview
print(df.info())

# Explore the published variable
print(df['published'])

# We need the four last characters of published in our new variable
df['year'] = df['published'].str[-4:]

# Convert from object (string) to integer
# We need this if we want to treat it as a number later on
df['year'] = df['year'].astype(int) 

# Check the year variable
print(df['year'].head(20))
