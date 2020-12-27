import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAIksA4t4r1JjjsVR0qwYkFq8wDGEtbp8Buo1pTxJrfvl8s8UJ_Qdwi5Jgsncn-efPxI4MuS2G0oaSihRlJKAFDrckn7-Y-rkB8v3hhRoSH1W6VenizbqqPUClXcsrCtsWQQar4Y2vCAfjutkq_AaIPOFh5HlkBN_PekrdSheaws1CszNp2apvaZOORexskxcElLA2F9T9fIJ3t4KbEdFoSSdveyx1Absa_0ozvKlrfFZHXaZXvJD6rCHI_Zjgdd4dV-zr36n7U-ZBerA',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

params = (
        ('q', 'Lose Yourself Eminem'),
        ('type', 'track'),
				('limit', 1)
    )

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params

print(response) # OK if 200

json_data = json.loads(response.text) # convert json response to text/dict

# Isolate track id for Rude Boy by Rihanna
trackid = json_data['tracks']['items'][0]['id']

# Setting parameters
params = (
    ('seed_tracks', trackid),
)
 
response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) # Making request
json_data = json.loads(response.text) # Converting response into Python data structure
 
# Printing the tracks by artists, one by one
for track in json_data['tracks']:
	print(track['album']['artists'][0]['name'],'by',track['name'])
