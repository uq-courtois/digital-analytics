import pandas as pd

data = [
	{'name':'Jack','grade':'A'},
	{'name':'Jack','grade':'B'},
	{'name':'Jack','grade':'C'},
	{'name':'Ann','grade':'A'},
	{'name':'Ann','grade':'A'},
	{'name':'Ann','grade':'A'},
	{'name':'Trevor','grade':'B'},
	{'name':'Trevor','grade':'B'},
	{'name':'Trevor','grade':'A'},
]

data = pd.DataFrame(data)

print(data)

# All grades per person are combined into a single string value
# The use of an lambda function is explained in depth later in this module
grouped = data.groupby('name', as_index=False)['grade'].apply(lambda x: ','.join(x))

# We use a function to count the occurences of 'A' per entry
# The use of an lambda function is explained in depth later in this module
grouped['Acount'] = grouped['grade'].apply(lambda x: x.count('A'))

print(grouped)
