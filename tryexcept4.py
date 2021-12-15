x = [
	{'name':'Jean','size':170},
	{'name':'Kim'},
	{'name':'John','size':180},
	]

for i in x:
	try:
		i['size'] = i['size'] + 5
		print(i['size'])
	except:
		pass
