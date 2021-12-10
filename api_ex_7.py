import json
import requests
import pandas as pd

# Reading data from csv
data = pd.read_csv('https://www.digitalanalytics.id.au/static/files/4_1.csv',sep=',') 
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values() 

# Use your own token - this one has expired
token = 'BQBX7lQdcVMv2GvwAjB-dSoU_eW72V5m7vop32fSN2eCcXKhTbilosrYb3kWR_aI4_6I1rwJeu-8hz3zdmPw6Xuud9FZVAN6OsSoXBemGYkmIJIimceEzaZyEcQkYuD7TkUtIl0v7LlsHiSdTO_rVIwxp0ogzWqmbSgpG2JJB48_0ImK2Zyneo62zaDLzUld-3lYzMjy493HIbYSZYps4J-yMTL-hIH_CLY2AtaoZqAglQlWBDJDk5j4DVJIdjSEKUE2WbvURkp1Ip892B-bN2c'
 
# Iterate through the imported data
for item in data:
	print('Searching for',item['Artist'])
 
	headers = {
    	'Accept': 'application/json',
    	'Content-Type': 'application/json',
    	'Authorization': 'Bearer ' + token,
	} 
 
	params = (
	# Per iteration, the value of q is the value of Artist in the iterator variable 
	# (one row in the dat file)
	('q', item['Artist']), 
	('type', 'artist'),
	)
 
	response = requests.get('https://api.spotify.com/v1/search',headers=headers, params=params) # request the response
	# The endpoint base url is supplemented by the arguments in the variables headers and params
 
	print(response) # OK when 200
 
	json_data = json.loads(response.text) # Convert json response to text/dict
 
	genres = json_data['artists']['items'][0]['genres'] # Isolating the genre information - as a list

	print(item['Artist'],genres)
	print()
