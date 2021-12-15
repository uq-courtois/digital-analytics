from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd # Added to be able to write a csv file 

# An empty list to store the results
data = []

for i in range(1,248):
	url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2021-01-01,2022-01-01&start='+str(i*50)+'&ref_=adv_nxt'
	print(url)

	def scraper(url):
	
		headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		req = Request(url, headers=headers)
		context = ssl._create_unverified_context()
		
		uClient= urlopen(req, context=context)
		html = uClient.read()
		uClient.close()
	
		return BeautifulSoup(html, 'html.parser')

	# The url that is compiled above and changes per iteration is requested
	soup = scraper(url)

	for h3 in soup.find_all('h3',class_='lister-item-header'):
		title = h3.find('a').getText()
		print(title)
		
		# Adding each title to the list of dictionaries with a title and url key-value pairs
		data.append({
			'title':title,
			'url':url,
			}
			)

		# Writing that list of dictionaries into a CSV file
		writedata = pd.DataFrame(data) 		
		writedata.to_csv('imdbdata.csv',sep=',',index=False) 
