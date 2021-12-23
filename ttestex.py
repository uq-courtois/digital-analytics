import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats
 
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/youtube_vevo_clean.csv', delimiter = ',') 
 
### BAR PLOTS OF TWO GROUPS FOR A VARIABLE
 
# Subset two groups
group1 = df[df['artist']=='ArianaGrandeVevo']['views']
group2 = df[df['artist']=='TaylorSwiftVEVO']['views']
print('Group means:',round(group1.mean(),2),round(group2.mean(),2))
print('Group stds:',round(group1.std(),2),round(group2.std(),2))

degreesoffreedom = (len(group1)+len(group2)-2)
print('Degrees of freedom',degreesoffreedom)

means = (group1.mean(),group2.mean()) # Calculating means
positions = [0, 1] #Defining positions in the graph
plt.bar(positions, means) # Compiling the plot
plt.xticks(positions,['ArianaGrandeVevo', 'TaylorSwiftVEVO'],rotation="horizontal") # Adding labels
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) # Prevent scientific notation
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig("barmeanstd.pdf") # Save figure
plt.clf() # Clear figure
 
# Calculate and print Welch’s t-test
print(stats.ttest_ind(group1, group2, equal_var = False))
