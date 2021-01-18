from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# Set default value
pagenumber = 0

# Continue looping as long as pagenumber is snmaller or equal to 3
while pagenumber <= 4:

  # The URL we want to scrape with a custom pagenumber (needs to be converted to str() to be able to concatenate it)
  url = 'https://www.pm.gov.au/media?page='+str(pagenumber)

  #################################################
  #################################################
  ### COPY/PASTE THIS BLOCK AS IS

  # Open URL (i.e., make request) + disguise agent
  headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
  req = Request(url, headers=headers)
  context = ssl._create_unverified_context()

  # To fetch html and store in variable 'html'
  uClient= urlopen(req, context=context)
  html = uClient.read() # html is stored in variable html
  uClient.close()

  #################################################
  #################################################

  ### Interpret the page source as html
  soup = BeautifulSoup(html, 'html.parser')

  print('Requested page',url)
    
  for item in soup.find_all('div',class_='media-title'):
    print('https://www.pm.gov.au/'+item.find('a')['href'])
      
  # Updating pagenumber for next loop
  pagenumber += 1
