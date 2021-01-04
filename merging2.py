import pandas as pd

df1 = pd.read_csv('imdb_data_1.csv',sep=';')
df2 = pd.read_csv('imdb_data_2.csv',sep=';')

print(df1.info()) # 4 variables, 19342 rows
print(df2.info()) # 6 variables, 19335 rows

# Integrate based on title, year, duration combinations
# Cases in df1 take priority, we want to enrich them with data fro df2
# That is why we merge 'left', so based on df1
df = pd.merge(df1, df2, how="left", on=['title', 'year', 'duration'])

# Same 7 unique variables, 19342 rows
print(df.info()) 
print(df)
