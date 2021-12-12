import pandas as pd
 
# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube_vevo.csv',sep=',')

# Function to categorise: receives views, returns view_cat 
def viewcat(views):
	if views >= 1000000:
		view_cat = 1
	else:
		view_cat = 0
	return view_cat

# Function to categorise: receives title, returns lyric_video
def lyric_video(title):
	if 'lyric video' in title.lower():
		print(title)
	else:
		lyric_video = 'no'
	return lyric_video

df['view_cat'] = df['views'].apply(lambda x: viewcat(x))
df['lyric_video'] = df['title'].apply(lambda x: lyric_video(x))

print(df[['view_cat','lyric_video']])
