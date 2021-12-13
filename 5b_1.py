import pandas as pd
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

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
text_tokens = word_tokenize(text)

# Remove stopwords from the tokenised text
wordlist = [word for word in text_tokens if not word in stopwords]

# Generate dataframe with extracted keywords, sorted for frequency
df = pd.DataFrame(list(dict(Counter(wordlist)).items()),columns = ['Word','Frequency']).sort_values(['Frequency'],ascending=False)

# Print df
print(df[['Word','Frequency']].head(50))
  
# Save to CSV file
df.to_csv('results.csv',sep=',',index=False)
