import json
import requests

# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQAn9b3t_lktBWrcYUVJUzwKkt9vzSp4ThKIXIP1jelMtumhBofoH_gRhXxbJKXYPruPJoI9BQbqtOw-aXdpn7DmlcO-huZ8vonkkI5ySVOqynmmhInTFhONwa4yotEHUa5BJZI11haR6ESn29i3g-4R4paeF9tCFnU'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 

# Set parameters
params = (
        ('q', 'Eminem Lose Yourself'),
        ('type', 'track'),
	('limit', '1'),
    )

# Make request
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Isolating the required information
trackid = data['tracks']['items'][0]['id']
print(trackid)
print() # Prints a blank line

# Now use that trackid to get recommendations from Spotify
# The token, headers, and imports can all stay the same as above
# (You can paste them in again, it won't affect the output)

# Set new parameters, for recommendations endpoint
params = (
    ('seed_tracks', trackid),
    ('limit', '10'), # Get the first 10
)

# Make request for recommendations
response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) 

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Loop through the tracks and print the artist and track name for each recommendation
for track in data['tracks']:
 artist_name = track['album']['artists'][0]['name']
 track_name = track['name']
 print(artist_name + ': ' + track_name)
