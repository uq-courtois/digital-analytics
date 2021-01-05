import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
### MEAN, STANDARD DEVIATION (std), MEDIAN (50%)
print(df['like'].describe())
 
### HISTOGRAM
# Render histogram (By increasing the bins number, you smoothen the graph)
plt.hist(df['like'], bins=100)

# Tidying up plot
plt.ticklabel_format(style='plain')
plt.xticks(rotation='vertical')
plt.tight_layout()

# Save figure as pdf
plt.savefig('histo.pdf')
 
plt.clf() # Clear figure
