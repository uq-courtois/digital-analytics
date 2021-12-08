# Import pandas
import pandas as pd
 
# Reading data from csv
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2_6.csv',sep=',')
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values() 

# Loop through data
for d in data:
    # Replace punctuation marks in string varibales of artist and song_title
    # Replace the / with a space to separate the words
    # Replace the ( and ) with nothing to remove them
    d['song_title'] = d['song_title'].replace('/', ' ')
    d['song_title'] = d['song_title'].replace('(', '')
    d['song_title'] = d['song_title'].replace(')', '')
    d['artist'] = d['artist'].replace('/', ' ')
    d['artist'] = d['artist'].replace('(', '')
    d['artist'] = d['artist'].replace(')', '')

    # Print updated values to check
    print(d['song_title'],'by',d['artist'])

# Converting temporary list of dictionaries into dataframe
newdata = pd.DataFrame(data)
# Writing dataframe into CSV file
newdata.to_csv('songinfo_clean.csv', sep=',', index=False)
