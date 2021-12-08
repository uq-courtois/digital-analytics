
import json
import requests

# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQBSWJohULY451Oj_Ej81Fu8GBZRoubiPZyIklSzrqL5tpgDA3kxiRX5jZFRKWmWyDgOg0R8C-jL83ELEOzSnX9GOEErb9Q1JMVKk3K_n4ZErEl-_bWD3Y4d2UDVcOLc2BpSD7IqGMHYB4sbvEIg-O8XQNpRn49992KGIHeXQKtJjEM_S7EreiX6byi-ICUj1QfNvr1oZ88UEYKsSlq5Ko5VH2T0uZfWrcJhXi3DNZpqyAT5raMnssQvRdz6RLrXA3iZDLpnijDhx80TtEW51Jc'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
params = (
        ('q', 'Taylor Swift'),
        ('type', 'artist'),
	('limit', '1'),
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Isolating the genre information and printing it - which is a list
genres = data['artists']['items'][0]['genres']
print(genres)

# The artist id
artistid = data['artists']['items'][0]['id']
print(artistid)
