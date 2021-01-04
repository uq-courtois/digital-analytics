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
grouped = data.groupby('name')['grade'].apply(lambda x: ','.join(x))

# The series (because just one variable) is transformed into a datagrame
grouped = grouped.to_frame()

# We use a function to count the occurences of 'A' per entry
# The use of an lambda function is explained in dept later in this module
grouped['Acount'] = grouped['grade'].apply(lambda x: x.count('A'))

print(grouped)
