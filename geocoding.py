### Credentials: https://developers.google.com/maps/documentation/geocoding/get-api-key#get-the-api-key
 
import json
from urllib.request import urlopen

# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 

# Build query for address argument
query =  'University of Queensland St Lucia'
# Replace spaces in query with +
query = query.replace(' ','+') 

# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyDC60i9o-E4sOVCsYCZCYGB3DIlhAenZy0" 

# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)

# Send request + get response
response = urlopen(compiledurl) 

# Convert JSON result -> our data are in the variable data
data = json.load(response) 

# Print data variable with hierarchical formatting
print(json.dumps(data, sort_keys=True, indent=3)) 
