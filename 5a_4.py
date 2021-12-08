import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/duplicates.csv',sep=',')

# Print the dataframe contents
print('\nDF before:\n',df)

# Print number of exact duplicates
print('\n# Exact duplicates:',df.duplicated().sum()) 

# Print rows with duplicates
print('\nRows with duplicates:\n',df[df.duplicated()])

# Drop exact duplicates
df = df.drop_duplicates()

# Print the dataframe contents
print('\nDF after:\n',df)
