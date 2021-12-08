import requests
import json
 
# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQC1QTZjM5Nf16au_6CHhTFrdhDVBhhjxfDj15Zy_JsEMoAM4KA5h9qQHmgUFAA2YdtVfwDfGcUfeN7TSuDTHtlOW6E4xQn2n7ebVz1HzRBvZgCDbRJ8MRLGUj0618uRpCKsmvxmpBavovlu8g6Kzp6aEn3nMJX2wriMp4UKcBvZz_THgYhx5J0YezCp2ObWzBtHA0JbGHylxekQ9HyL6eBboZlI4s7XdsGeT-KEwpR32w6LW2NWPwmyn67QanZFUirp4zsBZu1WtHP2KZK8b-8'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
}

# Add in the trackid, here we use the one for Taylor Swift's Shake it off
trackid = "0cqRj7pUJDkTCEsJkx8snD"

# Setting parameters
params = (
    ('seed_tracks', trackid),
)

# Making request
response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) 

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Print result
print(json.dumps(data, sort_keys=True, indent=3)) 
