x = ['1,345','1.345K','1,345,000','1.345M']

for i in x:
	i = i.replace(',','')

	if 'K' in str(i):
		i = i.replace('K','')
		i = int(float(i)*1000)

	if 'M' in str(i):
		i = i.replace('M','')
		i = int(float(i)*1000000)

	print(i)
