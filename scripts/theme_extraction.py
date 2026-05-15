import pandas as pd
from collections import Counter
import re

# Load sentiment dataset
df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# Focus only on negative reviews
negative_reviews = df[df["sentiment"] == "Negative"]["review"]

# Basic keyword cleaning
words = []

for review in negative_reviews:
    review = str(review).lower()
    review = re.sub(r'[^a-zA-Z\s]', '', review)

    for word in review.split():
        if len(word) > 3:
            words.append(word)

# Count most common complaint words
common_words = Counter(words).most_common(30)

print("\n=== Top Complaint Keywords ===\n")

for word, count in common_words:
    print(f"{word}: {count}")