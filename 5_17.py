import researchpy as rp
import matplotlib.pyplot as plt
import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
# Print df info to get a variable overview
print(df.info())
 
# We need the four last characters of published in our new variable
df['year'] = df['published'].str[-4:]
df['year'] = df['year'].astype(int)
 
 
def yearcat(x):
	if x >= 2005 and x < 2010:
		y = '2005 until 2010'
	if x >= 2010 and x < 2015:
		y = '2010 until 2015'		
	if x >= 2015:
		y = '2015 until now'
	return y
 
df['yearcat'] = df['year'].apply(lambda x: yearcat(x))

### MODE, FREQUENCIES, AND COUNTS
catsum = rp.summary_cat(df['yearcat'])
print(catsum)

### BART CHART
plt.bar(catsum['Outcome'],catsum['Percent'])
plt.ylabel('Percentage')
 
# Saving the image to a file
plt.savefig('barchart.pdf')
plt.clf() # Clear figure
