# Note: for every exercise on scraping, you can re-use this
# block of code to make the request and get html.
# The html is stored in the variable 'soup'. When you 
# use this code, you might want to #hash out the line
# with print(soup), not to clutter your console.

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) 
		 AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# Add in the url you want to scrape
soup = scraper('https://digitalanalytics.id.au/static/materials/beyonce/index.html')

print(soup) # Prints the html in the console
