# Import pandas
import pandas as pd
 
# Reading data from csv
data = pd.read_csv('http://digitalanalytics.id.au/static/files/2_5.csv',sep=';')
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values()

# Create empty list to store domains
domains = []
 
# Iterate through the imported data
for item in data:
	# Split on forward slash and keep first index to extract domain
	# Store in variable domain
	domain = item['URL'].split('/')[0]
	# Append variable domain to list domains, iteration per iteration
	domains.append(domain)

# Convert list to set and back to list to filter duplicates
print(list(set(domains)))
