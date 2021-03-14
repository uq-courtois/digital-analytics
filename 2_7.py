# Import pandas
import pandas as pd
 
# Reading data from csv
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2_6.csv',sep=';')
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values() 

# Loop through data
for d in data:
	# Replace non-string characters in values of followers and following key values with suitable numerical equivalents. 
	# K = 1000, so replaced by 000
	# M = 1000000, so replaced by 000000
	# Get rid of the . altogether
	d['followers'] = d['followers'].replace('K','000')
	d['followers'] = d['followers'].replace('M','000000')
	d['followers'] = d['followers'].replace(',','')
	d['following'] = d['following'].replace('K','000')
	d['following'] = d['following'].replace('M','000000')
	d['following'] = d['following'].replace(',','')

	# Print updated version of the dictionary to check
	print(d)

# Converting temporary list of dictionaries into dataframe
newdata = pd.DataFrame(data) 
# Writing dataframe into CSV file
newdata.to_csv('instagram_clean.csv',sep=';',index=False) 
