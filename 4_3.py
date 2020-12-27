import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQBw0yD2iV67wqzgjYXkET17RhZv65BgjidA3j2r_qQRjDE-MFrfqtgAiUfuwBR9krCRrI7VOiIlNQfd2kekI-Jtf5oO09nQhAdOwC0KX9L43RVc7ANcLw6i6sf7qDFvZPeXo4EYCv_20hEHM9XLpqUItShTc9UOmkpxfpJ6FAmqHKNlnjNw65iB7f_AUow0finEpyEKPhebeJGAe84eGPNoAXfLMp-7waoow7Pce7LDQjiadSTcRcXiuXjr7GxNAVEYT-YU0VQ1HWrf4Q',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

params = (
        ('q', 'Rihanna'),
        ('type', 'artist'),
	('limit', 1)
    )

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params

json_data = json.loads(response.text) # convert json response to text/dict

# Isolate image location
imgurl = json_data['artists']['items'][0]['images'][0]['url']

# Create a new, empty picture file
imgfile = open('rihanna.jpg','wb')
# Write picture information into empty file
imgfile.write(urlopen(imgurl).read())
# Close file
imgfile.close() 

print('Image saved')
