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

# Add in appropriate url
soup = scraper('https://www.digitalanalytics.id.au/static/materials/imdb/')

# Isolate div with filmography items
filmography = soup.find('div',class_='filmo-category-section')

# Get all links from filmography div and loop through them
for a in filmography.find_all('a'):
	print(a.getText())
