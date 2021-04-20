from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import json
 
url = 'https://www.imdb.com/title/tt0386676/' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
soup = BeautifulSoup(html, 'html.parser')

jsonobject = soup.find('script',type='application/ld+json').string
imdbdata = json.loads(jsonobject)

print(json.dumps(imdbdata, sort_keys=True, indent=3))
