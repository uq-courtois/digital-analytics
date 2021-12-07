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

soup = scraper('https://digitalanalytics.id.au/static/materials/')

# Find and loop through all the img elements
for i in soup.find_all('img'):

	# Get the img url from the img source attribute
	imgurl = i['src']
	print(imgurl)
	
	# Isolate file name, using the text right after the last / in the url
	filename = imgurl.split('/')[-1]

	# Create a new, empty picture file in project
	imgfile = open(filename,'wb') 

	# Write picture information into empty file
	imgfile.write(urlopen(imgurl).read())

	# Close file 
	imgfile.close() 
