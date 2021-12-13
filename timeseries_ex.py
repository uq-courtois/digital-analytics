import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube_vevo_clean.csv',sep=',')

### Displaying time series
 
# Calculate mean, minimum, and maximum ratings per year (groupby)
like_mean = df.groupby('year', as_index=False)['like'].mean()
dislike_mean = df.groupby('year', as_index=False)['dislike'].mean()
 
# Plot these variables together
plt.plot(like_mean['year'],like_mean['like'],label="Mean likes")
plt.plot(dislike_mean['year'],dislike_mean['dislike'],label="Mean dislikes")
 
# Add a legend
plt.legend()
 
# Forces tidy plot lay-out
plt.tight_layout()
 
# Save the figure
plt.savefig('timeseries.pdf')
