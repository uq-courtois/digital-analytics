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

soup = scraper('https://digitalanalytics.id.au/static/materials/justin/')

# Step 1: Narrow down the HTML in soup to the minimum
divofinterest = soup.find('div',class_='YAJzu _26IxR _2QLX-')

# Step 2: Loop though divofinterest and look for all divs with class name _2wWGp
for d in divofinterest.find_all('div',class_='_2wWGp'):
	print(d)
	print()
