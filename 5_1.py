import pandas as pd

# Reading files
df1 = pd.read_csv('mtv-artists_a.csv',sep=',') 
df2 = pd.read_csv('mtv-artists_b.csv',sep=',')

# Check and compare variables: same quantity and names?
print(df1.info())
print(df2.info())

# Appending
df = df1.append(df2)

print(df1.shape) # Shape of first df, 2000 rows, 6 variables
print(df2.shape) # Shape of second df, 2999 rows, 6 variables
print(df.shape) # Shape of integrated df, 4999 rows, 6 variables

df.to_csv('mtv-integrated.csv',sep=';',index=False) # Save file
