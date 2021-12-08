import json
from urllib.request import urlopen

# To make the code shorter in this snipper, the request url is hardcoded
requesturl = 'https://maps.googleapis.com/maps/api/geocode/json?address=University+of+Queensland+St+Lucia&key=AIzaSyB_kohrkvQDmgFaqHIOcJkFNCnolK7xRq4'

# Send request + get response
response = urlopen(requesturl) 

# Convert JSON result
data = json.load(response) 
data = data['results']

print(json.dumps(data, sort_keys=True, indent=3)) 
