import pandas as pd

# Read file
df = pd.read_csv('youtube_vevo.csv',sep=';') 

# Print df info to get a variable overview
print(df.info())

def likeratio(x,y):
	if x > y:
		z = 'More likes'
	if x < y:
		z = 'More dislikes'
	if x == y:
		z = 'Equal likes and dislikes'
	return z

df['likeratio'] = df.apply(lambda x: likeratio(x['like'],x['dislike']),axis=1)

# Print likes, dislikes, and likeratio
print(df[['like','dislike','likeratio']])
