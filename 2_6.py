import pandas as pd
 
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2_5.csv',sep=',')
data = data.T.to_dict().values() 

for i in data:
	# Conditional to only process rows with a rank smaller than or equal to three
	if i['Rank'] <= 3:
		print(i)
