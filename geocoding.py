### Credentials: https://developers.google.com/maps/documentation/geocoding/get-api-key#get-the-api-key
 
import json
from urllib.request import urlopen

# Endpoint URL
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" 

# Build query for address argument
query = "address=" + "University of Queensland St Lucia" 
# Replace spaces in query with +
query = query.replace(' ','+') 

# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "&key=AIzaSyDC60i9o-E4sOVCsYCZCYGB3DIlhAenZy0" 

# Combining all the url components into a single url
compiledurl = baseurl + query + apikey 

# Send request + get response
json_object = urlopen(compiledurl) 

# Convert JSON result
locationdata = json.load(json_object) 
 
print(locationdata)

# Use this print below to have the response nicely formatted
# print(json.dumps(locationdata, sort_keys=True, indent=3)) 
