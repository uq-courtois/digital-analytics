import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQBC2Oc2eT844q3oMruiSuWUOfwVw_dA70NzkDSucLC-YDC_bp4RsRYfdHVdv_M9HoYXK9l6saikvYb3whF5nLIYOdMLiClA951enkNL2h0XvF257cgKqKDrdCvsp-LX9kghWCTXId94N3PWCygZ4cYfumDItyYK0pJ2IpQSUObC7ojfJ93CRQZyI6UcytW__rjY9K6v1c_oRvcnLU_-eMRALYNuj4mbHOg4yvgR5mEu-K69l4pOLfuAtYL1ZwjyPUDsXK06BVM3RL6XDA',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

# Set id for Rude Boy by Rihanna (assume you know)
trackid = '60jzFy6Nn4M0iD1d94oteF'

# Setting parameters
params = (
    ('seed_tracks', trackid),
)
 
response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) # Making request
print(response) # Optional, informs on whether call was successful (Code [200])
json_data = json.loads(response.text) # Converting response into Python data structure
 
# Printing the tracks by artists, one by one
for track in json_data['tracks']:
	print(track['name'],'by',track['album']['artists'][0]['name'])
