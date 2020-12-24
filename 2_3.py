# Import pandas
import pandas as pd

# Hard-coded data in list of dictionaries
data = [
	{'Name':'Mark','Course':'Math','Grade':'A'},
	{'Name':'Mark','Course':'English','Grade':'A'},
	{'Name':'Eric','Course':'Math','Grade':'B'},
	{'Name':'Eric','Course':'English','Grade':'B'},
]

# Converting list of dictionaries into dataframe
data = pd.DataFrame(data)
# Writing dataframe into CSV file
data.to_csv('grades.csv',sep=';',index=False) 
