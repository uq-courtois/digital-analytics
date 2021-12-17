import pandas as pd
 
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2_5.csv',sep=',')
data = data.T.to_dict().values()

for item in data:
	# Split on forward slash and keep first index to extract domain
	domain = item['URL'].split('/')[0]
	print(domain)
