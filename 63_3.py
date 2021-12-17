import pandas as pd
data = pd.read_csv('csvtutorial.csv',sep=',')
data = data.T.to_dict().values()
