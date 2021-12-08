# Import pandas
import pandas as pd

# Hard-code data into list of dictionaries
data = [
	{'User':'Mark','Followers':234,'Following':145},
	{'User':'Eric','Followers':129,'Following':138},
	{'User':'Lisa','Followers':194,'Following':453},
	{'User':'Achmad','Followers':123,'Following':194},
]

# Loop through data
for d in data:
	# Per iteration print number of followers
	print(d['User'],'has',d['Followers'],'followers')

# Converting list of dictionaries into dataframe
data = pd.DataFrame(data)
# Writing dataframe into CSV file
data.to_csv('instagram.csv',sep=',',index=False) 
