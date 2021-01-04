import pandas as pd

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

data = pd.DataFrame(data)

print(data)

grouped = data.groupby(['name']).sum()

print(grouped)
