import researchpy as rp
import matplotlib.pyplot as plt
import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
### CORRELATION
print(rp.correlation.corr_pair(df[['views', 'like']]))
 
# The r-value is the magnitude of the correlation
# p-value expresses statistical significance level
# N reports number of cases the analysis is based on
 
### SCATTERPLOT
plt.scatter(df['views'],df['like']) # Build plot
plt.xlabel('Number of views') # x-axis label
plt.ylabel('Number of likes') # y-axis label

# Gets rid of scientific notation
plt.ticklabel_format(style='plain')
# Rotates labels vertically
plt.xticks(rotation='vertical')
# Forces tidy plot lay-out
plt.tight_layout()


plt.savefig('scatterplot.pdf') # Save figure
plt.clf() # Clear figure
