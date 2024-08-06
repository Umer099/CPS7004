import nltk
from nltk.corpus import stopwords
from week7.tokenizer import tokens

# Download the stop words
nltk.download('stopwords')

# Create a set containing English stop words for filtering
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Display the filtered tokens
print(f'{'Filtered Tokens':25}: {filtered_tokens}')