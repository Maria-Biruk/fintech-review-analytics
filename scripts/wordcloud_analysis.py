import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/clean_reviews.csv")

# Combine all reviews into one text
text = " ".join(df["review"].dropna().astype(str))

# Clean text
text = text.lower()
text = re.sub(r"[^a-zA-Z\s]", "", text)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Plot
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Bank Reviews")
plt.show()