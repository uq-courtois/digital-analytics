urls = []

for i in range(1,248):
	url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2021-01-01,2022-01-01&start='+str(i*50)+'&ref_=adv_nxt'
	print(url)

	urls.append(url)
