import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv', delimiter = ',') 

# Set max of rows to show, in/decrease to needs
pd.set_option('display.max_rows', 9999) 
 
# CROSSTABULATION
table, results = rp.crosstab(df['view_cat'],df['lyric_video'], prop= 'col', test= 'chi-square')
 
print(table) # Prints crosstab
print()
print(results) # Prints statistics tab
 
# STACKED BAR CHART
ct = pd.crosstab(df['lyric_video'],df['view_cat'],normalize='index') # Create PD crosstab as basis for plot
ct.plot.bar(stacked=True) # Generate plot
plt.legend(loc='lower left', bbox_to_anchor= (0.0, 1.01),frameon=False) # Tidy up legend (other)
plt.xticks(rotation="horizontal") # Horizontal x-axis labels
plt.xlabel('Lyric video') # Adding label on x-axis
plt.ylabel('Viewer categories') # Adding label on y-axis
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig('stackedbar.pdf') # Saving figure
 
# Clear figure
plt.clf() 
