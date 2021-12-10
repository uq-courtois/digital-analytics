import json
import requests
import pandas as pd

# Reading data from csv
data = pd.read_csv('http://112.213.36.202/static/files/4_1.csv',sep=';') 
# Converting dataframe into list of dictionaries
data = data.T.to_dict().values() 

# Use your own token - this one has expired
token = 'BQB_L23a4yd4rH_6Wb2rDNccymwTM5YG-Inn3CJfWGOAlabNx3_VzFyGVO-oM6RgAG3VXa9mfdCWCe7aOkcIQ4ns9TMPKV0Sq0dp4SxKeJS4I3UrJXvctCjY4mnGoC2_Fb9lenQdBUvSQK5sKfjyZHakZ_yBAXXvdN3s7Rv5ozGDfZjGMpyZMUAFR8Mf8siuyD2i1F1vKTcwrRT9s3mud0e4bpH1gnOhzadc7CZoaRBUZbcEFnymNwgjLr8FrqYm8DqSjFMNV6POtiCNbvL8djg'
 
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
 
	json_data = json.loads(response.text) # convert json response to text/dict
 
	genres = json_data['artists']['items'][0]['genres'] # Isolating the genre information - as a list

	print(item['Artist'],genres)
