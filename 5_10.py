import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Print df info to get a variable overview
print(df.info())

# We need the four last characters of published in our new variable
df['year'] = df['published'].str[-4:]
df['year'] = df['year'].astype(int)


def yearcat(x):
	if x >= 2005 and x < 2010:
		y = 1
	if x >= 2010 and x < 2015:
		y = 2		
	if x >= 2015:
		y = 3
	return y

df['yearcat'] = df['year'].apply(lambda x: yearcat(x))

# Print both year and yearcat
print(df[['year','yearcat']])
