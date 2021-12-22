import pandas as pd

# Read file 1
df1 = pd.read_csv('imdb_data_a.csv',sep=',') 
# Read file 2
df2 = pd.read_csv('imdb_data_b.csv',sep=',')

print(df1.info()) # 10 variables, 13969 rows
print(df2.info()) # Same 10 variables, 19999 rows

df = df1.append(df2)

print(df.info()) # Same 10 variables, 33968 rows
