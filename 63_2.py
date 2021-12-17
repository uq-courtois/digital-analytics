import pandas as pd
data = pd.read_csv('https://digitalanalytics.id.au/static/files/csvtutorial.csv',sep=',')
data = data.T.to_dict().values()

for i in data:
  print(i)
