import pandas as pd

# Data entered as a list of dicts
data = [
	{'name':'Jack','expenditure':3},
	{'name':'Jack','expenditure':4},
	{'name':'Jack','expenditure':3},
	{'name':'Ann','expenditure':5},
	{'name':'Ann','expenditure':5},
	{'name':'Ann','expenditure':6},
	{'name':'Trevor','expenditure':3},
	{'name':'Trevor','expenditure':6},
	{'name':'Trevor','expenditure':7},
]

# List of dicts converted to Pandas dataframe
data = pd.DataFrame(data)

print(data)

# Appplication of grouping method
grouped = data.groupby(['name']).sum()

print(grouped)
