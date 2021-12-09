import json
from urllib.request import urlopen

# To make the code shorter in this snippet, the request url is hardcoded
# Remember this code snippet won't work unless you replace the API key with a valid new key
requesturl = 'https://maps.googleapis.com/maps/api/geocode/json?address=University+of+Queensland+St+Lucia&key=AIzaSyB_kohrkvQDmgFaqHIOcJkFNCnolK7xRq4'

# Send request + get response
response = urlopen(requesturl) 

# Convert JSON result
data = json.load(response) 
data = data["results"][0]["formatted_address"]

print(json.dumps(data, sort_keys=True, indent=3)) 
