from sklearn.feature_extraction.text import CountVectorizer

# Initialise CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the data
X = vectorizer.fit_transform(data)

# Convert to DataFrame for easy viewing
bow_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Print the resulting DataFrame
print(bow_df)

data = pre_processed_data.apply(lambda x: ' '.join(x))