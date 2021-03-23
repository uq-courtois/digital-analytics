from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
# The URL we want to scrape (CHANGED!)
url = 'https://www.discogs.com/label/19882-Sony' 
 
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
 
# The second div with class content contains the sublabels
sublabels = soup.find_all('div',class_='content')[1]

# Loop through all a-tags in sublabels
for sublabel in sublabels.find_all('a'):
	# Get href attribute from a-tag and combine with domain prefix
	print('http://www.discogs.com'+sublabel['href'])
