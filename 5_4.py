import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Show dataframe info
df = df.sort_values(by=['views'], ascending=False) 

# Print first 25 values of titles and views
print(df[['title','views']].head(25))

# Added for your information - not part of the exercise
# Suppose you want to include this as a table in a report...
# Copy/pasting from the console is a terrible mess
# We can save this info as a file and load it into MS Excel,
# format it, and then copy/paste it to MS Word

table = df[['title','views']].head(25)
table.to_csv("table.csv",index=False)

# Python makes life easier...
