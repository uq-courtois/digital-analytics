import pandas as pd # Module is needed, otherwise we get a NameError

# Hard-coded data in list of dictionaries
data = [
	{'Name':'Mark','Course':'Math','Grade':'A'},
	{'Name':'Mark','Course':'English','Grade':'A'},
	{'Name':'Eric','Course':'Math','Grade':'B'},
	{'Name':'Eric','Course':'English','Grade':'B'},
]

# Always make sure the variable within pd.DataFrame() has the same name as your list of dictionaries
data = pd.DataFrame(data)
data.to_csv('grades.csv',sep=',',index=False) 
