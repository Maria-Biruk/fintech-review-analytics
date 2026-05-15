import pandas as pd
import re
from collections import Counter

df = pd.read_csv("data/raw/clean_reviews.csv")

# Focus on ALL reviews (not just negative)
texts = df["review"].dropna()

keywords = []

for t in texts:
    t = str(t).lower()
    t = re.sub(r"[^a-zA-Z\s]", "", t)

    for word in t.split():
        if len(word) > 3:
            keywords.append(word)

common = Counter(keywords).most_common(30)

print("\n=== Feature/Request Keywords ===\n")
for w, c in common:
    print(w, c)