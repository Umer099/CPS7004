import nltk
from nltk.tokenize import word_tokenize


# Download the Punkt tokenizer models, which are necessary for tokenizing the text
nltk.download('punkt')

# Sample text to be tokenized
text = "I love learning about artificial intelligence and related topics."

# Tokenize the text into individual words and punctuation
tokens = word_tokenize(text)

# Display the list of tokens
print(f'{'Tokens':25}: {tokens}')