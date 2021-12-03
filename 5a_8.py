import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/headlines.csv',delimiter=',')

# DF before
print('\nBefore',df)

def categorisation(headline):
	if 'COVID' in headline:
		covid_mention = 'yes'
	else:
		covid_mention = 'no'
	return covid_mention

df['covid_mention'] = df['headline'].apply(lambda x: categorisation(x))

# The result
print('\nAfter',df)
