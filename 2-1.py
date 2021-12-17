import pandas as pd # Module is needed, otherwise we get a NameError
 
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2-1.csv',sep=',')
data = data.T.to_dict().values() 
 
for item in data:
	print(item)
