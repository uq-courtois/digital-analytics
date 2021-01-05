import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# All titles per artist are combined into a single string value
grouped = df.groupby('artist' , as_index=False,)['title'].apply(lambda x: ','.join(x))

# Count the instances of live per title, making sure we're looking in the .lower() version of the title
grouped['live'] = grouped['title'].apply(lambda x: x.lower().count('live'))

# Sort the values of the variable live in grouped in descending order
grouped = grouped.sort_values(by=['live'], ascending=False) 

# Printing the top 25
print(grouped[['artist','live']].head(25))
