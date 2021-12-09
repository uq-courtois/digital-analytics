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
soup = scraper('https://www.digitalanalytics.id.au/static/materials/billboard')

# Narrow down soup to the div that contains all the artist-song combinations
chartdata = soup.find('div',class_='chart-results-list // u-padding-b-250')

# Loop through the list items <li> with class name 'lrv-u-width-100p'
for li in chartdata.find_all('li',class_='lrv-u-width-100p'):
	# Extract the text from the <h3> tag with the song title
	# Because there are excess spaces in the string, we use the strip() method to clean that up
	print(li.find('h3').getText().strip())
	# Extract the text from the <span> tag with the song artist
	print(li.find('span').getText().strip())
	print()
