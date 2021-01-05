import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Print df info to get a variable overview
print(df.info())

# We need the four last characters of published in our new variable
df['year'] = df['published'].str[-4:]
df['year'] = df['year'].astype(int)

# Recode year into age (use 2021 as current year)
df['age'] = 2021 - df['year']

# Print year and age to check
print(df[['year','age']])
