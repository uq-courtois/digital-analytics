import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Show dataframe info
df = df.sort_values(by=['views'], ascending=False) 

# Print first 25 values of titles and views
print(df[['title','views']].head(25))
