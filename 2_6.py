import pandas as pd
data = pd.read_csv('https://www.digitalanalytics.id.au/static/files/2_6.csv',sep=',')
data = data.T.to_dict().values()

for i in data:
  i['surface'] = i['length'] * i['width']

newdata = pd.DataFrame(data)
newdata.to_csv('rectangles.csv',sep=',',index=False)
