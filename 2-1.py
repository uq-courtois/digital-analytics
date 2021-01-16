# Import pandas
import pandas as pd
 
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2-1.csv',sep=',')
# Reading data from csv (important - separator is a ,)
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries
 
# Iterate through the imported data
for item in data:
	print(item)
