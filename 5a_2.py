import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/artists-spotify.csv',sep=',')

# Get overall description of the dataframe
print(df.info())

# Loop through all columns and show unique values:
for c in df.columns.values.tolist():
	print('\n',len(df[c]),'unique values in variable:',c)
	print(df[c].unique())

# Get unique values for one particular variable
# You just need to replace the column name in the ''
print(df['recommended_artist'].unique())

# Get the number of unique values in a variable
print(len(df['recommended_artist'].unique()))

# Get overview of the first 5 and last 5 values of a variable
print(df['recommended_artist'])

# Get overview of the first 20 values of a variable:
print(df['recommended_artist'].head(20))

# Get overview of the last 20 values of a variable:
print(df['recommended_artist'].tail(20))

# Get overview of more than one variable
print(df[['recommended_artist','recommended_track']])
