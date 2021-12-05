from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# Add in the url you want to scrape
soup = scraper('http://www.digitalanalytics.id.au')

print(soup) # Prints the html in the console
