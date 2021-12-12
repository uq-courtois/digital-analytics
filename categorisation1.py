import pandas as pd
 
# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube_vevo.csv',sep=',')

# Function to categorise: receives views, returns view_cat 
def categorisation(views):
	if views > 1000000:
		view_cat = 1
	else:
		view_cat = 0
	return view_cat

# Create new variable based on views, applies function categorisation
df['view_cat'] = df['views'].apply(lambda x: categorisation(x))
print(df['view_cat'])
