import json
import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAfvDc85E84NETglzEnj-bjV5zITQa_QnNKy8CIczfrSorMQGeyzWR00D3y_G55T3j3U2tGVCFUmA4ECKhD-Y4lAc0v74y-QKWhGf7HCEnTLjiH4KBfF0y0TFg2NUftI1HG-ONARlModAphxt1utsPYb4_fprBc13ZHWvISbBhw-t4JLUC3ficPDkE8OZQasP0L6_5D3B7FJomzHt-MBQjR7oswDpzzLoZ5ebhr7EVe0x1qn1nX3R9JGRlr-_IYeGnZqxW-GukHWvvARw',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

params = (
        ('q', 'Rihanna'),
        ('type', 'artist'),
    )

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])

json_data = json.loads(response.text) # convert json response to text/dict

print(json_data['artists']['items'][0]['followers']['total']) # The returndata narrowed down for total number of followers
