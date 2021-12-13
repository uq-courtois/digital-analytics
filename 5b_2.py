import pandas as pd
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 
 
# Get stopwords
sw = pd.read_csv('https://www.digitalanalytics.id.au/static/files/stopwords.csv',sep=',')
stopwords = sw['stopwords'].tolist()
 
# Read data
df = pd.read_csv('https://digitalanalytics.id.au/static/files/headlines.csv',sep=',')
 
# Combine all values of 'headline' into a single string variable 'text'
text = ' '.join(df['headline'].tolist()).lower()
 
# Remove punctuation from string variable 'text'
text = text.translate(str.maketrans('', '', string.punctuation))
 
# Tokenise text (i.e., split up in list of words)
text_tokens = nltk.word_tokenize(text)
 
# Remove stopwords from the tokenised text
wordlist = [word for word in text_tokens if not word in stopwords]
 
# Extract ngrams into a list of dictionaries (use 2 for bigrams)
ngrams = []
for ngram in nltk.ngrams(wordlist, 2):
	ngrams.append({'Ngram':' '.join(ngram)})
 
# Get rid of duplicates ngrams
ngrams = [dict(t) for t in {tuple(d.items()) for d in ngrams}]
 
# Count and add frequencies to list of dicts
for ngram in ngrams:
	ngram['Frequency'] = text.count(ngram['Ngram'])
	
# Generate dataframe with extracted ngrams, sorted for frequency
df = pd.DataFrame(ngrams).sort_values(['Frequency'],ascending=False)
	
# Only keep ngrams with a frequency higher than 1
df = df [df['Frequency'] > 1]
	
# Print df
print(df[['Ngram','Frequency']].head(50))
	
# Save to CSV file
df.to_csv('results.csv',sep=',',index=False)
