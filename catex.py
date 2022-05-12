import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
 
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv', delimiter = ',') 
 
# Set max of rows to show, in/decrease to needs
pd.set_option('display.max_rows', 9999) 
 
### MODE, FREQUENCIES, AND COUNTS
catsum = rp.summary_cat(df['view_cat'])
print(catsum)
# Mode is value with highest count: 'USA'
# Counts are absolute frequencies
# Percentages are relative frequencies
 
### BART CHART
plt.bar(catsum['Outcome'],catsum['Count'])
# x-labels based on outcome strings of catsum
# bar height based on count figures of catsum
 
# Saving the image to a file
plt.tight_layout()
# Saving the image to a file
plt.savefig('view_cat-absolute-barchart.pdf')
# Clear figure
plt.clf() 
 
### BART CHART
plt.bar(catsum['Outcome'],catsum['Percent'])
# x-labels based on outcome strings of catsum
# bar height based on percentage figures of catsum
 
# Forces tidy plot lay-out
plt.tight_layout()
# Saving the image to a file
plt.savefig('view_cat-relative-barchart.pdf')
# Clear figure
plt.clf() 
