import nltk
from nltk.stem import WordNetLemmatizer
from week7.stop_word import filtered_tokens

# Download the relevant models
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create an instance of the WordNetLemmatizer class
lemmatizer = WordNetLemmatizer()

# Apply lemmatization to each word in the filtered_tokens list
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Display tokens
print(f'{'Lemmatized Tokens':25}: {lemmatized_tokens}')