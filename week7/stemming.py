from nltk.stem import PorterStemmer
from week7.stop_word import filtered_tokens

# Create an instance of the PorterStemmer class
stemmer = PorterStemmer()

# Apply stemming to each word in the filtered_tokens list
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Print the list of stemmed tokens to the console
print(f'{'Stemmed Tokens':25}: {stemmed_tokens}')