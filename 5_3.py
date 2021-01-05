import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Show dataframe info
print(df.info())
