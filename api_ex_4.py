import json
import requests
 
# Use your own token - this one has expired
token = 'BQB_L23a4yd4rH_6Wb2rDNccymwTM5YG-Inn3CJfWGOAlabNx3_VzFyGVO-oM6RgAG3VXa9mfdCWCe7aOkcIQ4ns9TMPKV0Sq0dp4SxKeJS4I3UrJXvctCjY4mnGoC2_Fb9lenQdBUvSQK5sKfjyZHakZ_yBAXXvdN3s7Rv5ozGDfZjGMpyZMUAFR8Mf8siuyD2i1F1vKTcwrRT9s3mud0e4bpH1gnOhzadc7CZoaRBUZbcEFnymNwgjLr8FrqYm8DqSjFMNV6POtiCNbvL8djg'
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Add in the trackid, here we use the one for Taylor Swift's Shake it off
trackid = "0U10zFw4GlBacOy9VDGfGL"
 
# Make request
response = requests.get('https://api.spotify.com/v1/audio-features/'+trackid, headers=headers)
 
# We want code [200] here, points to a successful request
print(response) 
 
# Convert response to text/dict
data = json.loads(response.text) 
 
# Print tempo value
print(data['tempo'])
