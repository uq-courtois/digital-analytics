# Import pandas
import pandas as pd
 
# Reading data from csv
data = pd.read_csv('http://112.213.36.202/static/files/2_5.csv',sep=';')
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values() 
 
# Create temporary empty list to store data rows with rank 1,2,3
rankdata = []

# Loop through data
for i in data:
	# Conditional to only process rows with a rank smaller than or equal to three
	if i['Rank'] <= 3:
		print(i)
		# Append the entire dictionary in the iteration to the list rankdata
		rankdata.append(i)

# Converting temporary list of dictionaries into dataframe
newdata = pd.DataFrame(rankdata) 
# Writing dataframe into CSV file
newdata.to_csv('ranks.csv',sep=';',index=False) 
