# IMPORT PANDAS
import pandas as pd
# READING FROM URL (Replace the url below with the url of the file you want to access)
data = pd.read_csv('https://digitalanalytics.id.au/static/files/csvtutorial.csv',sep=',')
data = data.T.to_dict().values()  # Converting dataframe into list of dictionaries
