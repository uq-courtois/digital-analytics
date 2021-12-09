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
 
soup = scraper('https://digitalanalytics.id.au/static/materials/mockup')

# Find all the <div> elements with class name 'newspost' and loop through them
for div in soup.find_all('div',class_='newspost'):

	# Get text from <a> (using <h2> here would work as well), write into title
	title = div.find('a').getText()

	# Get text from <p>, write into text
	text = div.find('p').getText()

	# Print both and leave a blank line
	print(title)
	print(text)
	print()
