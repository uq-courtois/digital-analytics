from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# Set empty artists list
artists = []

# Set default value
pagenumber = 1

# Continue looping as long as pagenumber is snmaller or equal to 3
while pagenumber <= 3:

	# The URL we want to scrape with a custom pagenumber (needs to be converted to str() to be able to concatenate it)
	url = 'https://www.discogs.com/label/2310-Aftermath-Entertainment?page='+str(pagenumber)+'&genre=All&limit=500'
	
	#################################################
	#################################################
	### COPY/PASTE THIS BLOCK AS IS
	
	# Open URL (i.e., make request) + disguise agent
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	# To fetch html and store in variable 'html'
	uClient= urlopen(req, context=context)
	html = uClient.read() # html is stored in variable html
	uClient.close()
	
	#################################################
	#################################################
	
	### Interpret the page source as html
	soup = BeautifulSoup(html, 'html.parser')
	
	# Loop through and isolate all artist td's and get the text
	# Append it to our list

	for artist in soup.find_all('td',class_='artist'):
		artist = artist.getText()
		artists.append(artist)
		print(pagenumber,artist)

	# End of iteration, update the pagenumber for the next iteration by adding 1
	pagenumber += 1

# Get rid of duplicates
artists = list(set(artists))

# Print the unique artists and the number of unique artists
print()
print('Unique artists:',artists)
print('Number unique artists:',len(artists))
