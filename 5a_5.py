import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/duplicates.csv',sep=',')

# Print the dataframe contents
print('\nDF before:\n',df)

# Print number of local duplicates in variable Artist
print('\n# Exact duplicates:',df.duplicated(subset=['Artist']).sum()) 

# Print rows with duplicates in variable Artist
print('\nRows with duplicates:\n',df[df.duplicated(subset=['Artist'])])

# Drop duplicates in variable Artist
df = df.drop_duplicates(subset=['Artist'])

# Print the dataframe contents
print('\nDF after:\n',df)
