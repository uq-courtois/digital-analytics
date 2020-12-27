  
# -*- coding: utf-8 -*-

import json
import requests
import pandas as pd

data = pd.read_csv('http://112.213.36.202/static/files/4_1.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

dataset = [] # Empty list to temporarily save the new data, and at the end write it into a new CSV

# Iterate through the imported data
for item in data:
	print('Searching for',item['Artist'])

	headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer BQBC2Oc2eT844q3oMruiSuWUOfwVw_dA70NzkDSucLC-YDC_bp4RsRYfdHVdv_M9HoYXK9l6saikvYb3whF5nLIYOdMLiClA951enkNL2h0XvF257cgKqKDrdCvsp-LX9kghWCTXId94N3PWCygZ4cYfumDItyYK0pJ2IpQSUObC7ojfJ93CRQZyI6UcytW__rjY9K6v1c_oRvcnLU_-eMRALYNuj4mbHOg4yvgR5mEu-K69l4pOLfuAtYL1ZwjyPUDsXK06BVM3RL6XDA',
	} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

	params = (
					('q', item['Artist']), # Per iteration, the value of q = the read artist
					('type', 'artist'),
			)

	response = requests.get('https://api.spotify.com/v1/search',headers=headers, params=params) # request the response
	# The endpoint base url is supplemented by the arguments in the variables headers and params

	print(response) # OK when 200

	json_data = json.loads(response.text) # convert json response to text/dict

	genres = json_data['artists']['items'][0]['genres'] # Isolating the genre information - as a list

	genres = ', '.join(genres) # To make a clean string out of the genres list

	print(item['Artist'])
	print(genres)
	print()
