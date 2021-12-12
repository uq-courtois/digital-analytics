import pandas as pd
 
# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube_vevo.csv',sep=',')

# Function to categorise: receives title, returns lyric_video
def lyric_video(title):
	if 'lyric video' in title.lower():
		lyric_video = 'yes'
	else:
		lyric_video = 'no'
	return lyric_video

df['lyric_video'] = df['title'].apply(lambda x: lyric_video(x))

print(df['lyric_video'])
