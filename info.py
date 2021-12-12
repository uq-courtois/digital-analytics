import pandas as pd
 
# Read data
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_nc.csv',sep=',')

print(df.info())
# 6343 rows/entries
# 7 columns/variables
# title is a categorical variable (i.e., string, object)
# views is a numeric variable (i.e., integer)
