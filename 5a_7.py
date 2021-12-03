import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/releaseyear.csv',delimiter=',')

# Print the dataframe
print(df.info())
print(df)

# Create new variable year
# Based on the existing variable release_year
# Grabs the fifth, fourth, third, and second to last digits
df['year'] = df['release_year'].str[-5:-1]

# Convert variable year to integer
df['year'] = df['year'].astype('int')

# Print result
print(df.info())
print(df)
