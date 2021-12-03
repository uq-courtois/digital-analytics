import pandas as pd

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/dob.csv',delimiter=',')

# DF before
print('\nBefore',df)

def age_cal(date_of_birth):
	age = 2021 - date_of_birth
	return age

df['age'] = df['date_of_birth'].apply(lambda x: age_cal(x))

# The result
print('\nAfter',df)
