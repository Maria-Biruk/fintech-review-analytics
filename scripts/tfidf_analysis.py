"""
TF-IDF thematic analysis for banking app reviews.
This script extracts important complaint themes from negative reviews.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# Select negative reviews only
negative_reviews = df[df["sentiment"] == "Negative"]["review"].dropna()

# TF-IDF vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=20
)

X = vectorizer.fit_transform(negative_reviews)

# Extract important keywords
keywords = vectorizer.get_feature_names_out()

print("\n=== Important Complaint Themes (TF-IDF) ===\n")

for word in keywords:
    print(word)