# IMPORT PANDAS
import pandas as pd
# READING FROM FILE NAME (Replace the name below with the name of the file you want to access)
data = pd.read_csv('csvtutorial.csv',sep=',')
data = data.T.to_dict().values()  # Converting dataframe into list of dictionaries
