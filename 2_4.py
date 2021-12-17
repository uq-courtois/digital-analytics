import pandas as pd # Module is needed, otherwise we get a NameError

# Hard-code data into list of dictionaries
data = [
	{'User':'Mark','Followers':234,'Following':145},
	{'User':'Eric','Followers':129,'Following':138},
	{'User':'Lisa','Followers':194,'Following':453},
	{'User':'Achmad','Followers':123,'Following':194},
]

for d in data:
	# Per iteration print number of followers
	print(d['User'],'has',d['Followers'],'followers')

# Always make sure the variable within pd.DataFrame() has the same name as your list of dictionaries
data = pd.DataFrame(data)
data.to_csv('instagram.csv',sep=',',index=False) 
