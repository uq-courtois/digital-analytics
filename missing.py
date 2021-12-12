import pandas as pd
 
# Read data
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_nc.csv',sep=',')

# Get summary of variables' missing data count
print('\n # Missing data:\n',df.isnull().sum())
 
# Print rows with missing data (add variable you want to inspect - here 'published')
isolatemissing = pd.isnull(df['published'])
print('\n Rows with missing data:\n',df[isolatemissing])

# But also also like, dislike, and url - We can just chuck this into a loop to make it as efficient as possible:
for i in ['published','like','dislike','url']:
	isolatemissing = pd.isnull(df[i])
	print('\n Rows with missing data:\n',df[isolatemissing])

# Drop rows with at least one missing value
df = df.dropna()
