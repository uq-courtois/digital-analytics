startnumbers = [1]

for i in range(1,247):
	startnumbers.append(i*50)

for sn in startnumbers:
	url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2021-01-01,2022-01-01&start='+str(sn)+'&ref_=adv_nxt'
	print(url)
