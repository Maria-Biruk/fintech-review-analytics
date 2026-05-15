import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv("data/raw/clean_reviews.csv")

# Sentiment function
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df["sentiment"] = df["review"].apply(get_sentiment)

# Save updated dataset
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print("\n=== Overall Sentiment ===")
print(df["sentiment"].value_counts())

print("\n=== Sentiment by Bank ===")
print(pd.crosstab(df["bank"], df["sentiment"]))

print("\nDONE")