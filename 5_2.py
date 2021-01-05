import pandas as pd

# Reading files
df1 = pd.read_csv('mtv-artists_genres.csv',sep=',') 
df2 = pd.read_csv('mtv-artists_socialmedia.csv',sep=',')

# Check whether there is a common variable (i.e., 'name')
print(df1.info())
print(df2.info())

# Merging
df = pd.merge(df1, df2, how='left', on=['name']) 
# combines vars from df1 and df2 based on shared values of variable name, df1 is the primary table

print(df1.shape) # Shape of first df, 2000 rows, 3 variables
print(df2.shape) # Shape of second df, 2000 rows, 4 variables
print(df.shape) # Shape of integrated df, 2000 rows, 6 variables

# Check non-nulls: do we have actual values for variables from both datafiles?
print(df.info())

df.to_csv('mtv-integrated.csv',sep=';',index=False) # Save file
