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

soup = scraper('https://digitalanalytics.id.au/static/materials/beyonce/index.html')

# From here on new code is added to the scraping snippet
table = soup.find('table')

for row in table.find_all('tr'):
	album = row.find('td',class_='album').getText()
	sales = row.find('td',class_='sales').getText()
	release = row.find('td',class_='release').getText()
	print(album,sales,release)
