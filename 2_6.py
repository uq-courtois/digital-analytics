import pandas as pd
data = pd.read_csv('https://www.digitalanalytics.id.au/static/files/2_5.csv',sep=';')
data = data.T.to_dict().values()

for i in data:
  if i['Rank'] <= 3:
    print(i['URL'])
