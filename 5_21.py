import researchpy as rp
import matplotlib.pyplot as plt
import pandas as pd
 
### GIVEN

# Read file
df = pd.read_csv('mtv-artists_genres.csv',sep=',') 

# Generate dataframe with counts per genre
x = df.groupby(['genre'], as_index=False)[['mtv']].count()
x = x.rename(columns={"mtv": "count"})

### YOU NEED TO DO THIS

# Sorting large to small
x = x.sort_values(by=['count'], ascending=False).head(25)

### YOU NEED TO ADAPT

# Generate a horizontal bar chart
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

y = tuple(x['genre'])
y_pos = np.arange(len(y))

ax.barh(y_pos, x['count'])
ax.set_yticks(y_pos)
ax.set_yticklabels(y)
ax.invert_yaxis()
ax.set_title('Top 25 Genres')

# Forces tidy plot lay-out
plt.tight_layout()

# Save the figure
plt.savefig('hbar.pdf')
