import researchpy as rp
import matplotlib.pyplot as plt
import pandas as pd
 
# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 
 
# We need the four last characters of published in our new variable
df['year'] = df['published'].str[-4:]
 
# Convert from object (string) to integer
# We need this if we want to treat it as a number later on
df['year'] = df['year'].astype(int) 

### Displaying time series
 
# Calculate sum of views per year
yv = df.groupby('year', as_index=False)['views'].sum()
 
# Plot these variables
plt.plot(yv['year'],yv['views'],label="Views")
# Adding in title
plt.title('Views per year')

# Gets rid of scientific notation
plt.ticklabel_format(style='plain')
# Rotates labels vertically
plt.xticks(rotation='vertical')
# Forces tidy plot lay-out
plt.tight_layout()

# Save the figure
plt.savefig('timeseries.pdf')
