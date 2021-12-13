import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
 
df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv', delimiter = ',') 

### CORRELATION
print(rp.correlation.corr_pair(df[['views', 'like']]))
 
# The r-value is the magnitude of the correlation
# p-value expresses statistical significance level
# N reports number of cases the analysis is based on
 
### SCATTERPLOT
plt.scatter(df['views'],df['like']) # Build plot
plt.xlabel('Number of views') # x-axis label
plt.ylabel('Number of likes') # y-axis label
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig('scatterplot.pdf') # Save figure
plt.clf() # Clear figure
