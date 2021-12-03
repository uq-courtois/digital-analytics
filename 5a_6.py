import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/missing.csv',delimiter=',')

# Print the dataframe contents
print('\nDF before:\n',df)

# Get summary of variables' missing data count
print('\n # Missing data:\n',df.isnull().sum())
 
# Print rows with missing data (add variable you want to inspect - here 'Song')
isolatemissing = pd.isnull(df['Song'])
print('\n Rows with missing data:\n',df[isolatemissing])

# Drop rows with at least one missing value
df = df.dropna()

# Print the dataframe contents
print('\nDF after:\n',df)
