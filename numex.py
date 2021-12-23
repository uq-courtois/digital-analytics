import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv', delimiter = ',') 
 
# Set max of rows to show, in/decrease to needs
pd.set_option('max_rows', 9999) 
 
### MEAN, STANDARD DEVIATION (std), MEDIAN (50%)
print(df['views'].describe())
 
### HISTOGRAM
# Render histogram (By increasing the bins number, you smoothen the graph)
plt.hist(df['views'], bins=100)

### Some optional lay-out tricks
### (this is new...)
# Avoid scientific notation 
plt.ticklabel_format(style='plain')
# Lay out labels vertically
plt.xticks(rotation='vertical')

# Forces tidy plot lay-out
plt.tight_layout()
# Save figure as pdf
plt.savefig('histo_views.pdf')
# Clear figure
plt.clf() 
