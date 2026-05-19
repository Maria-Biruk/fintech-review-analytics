import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:94128870@localhost:5432/bank_reviews"
)

# Load reviews
df = pd.read_sql("SELECT * FROM reviews", engine)

# Convert rating column to numeric
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Load banks
banks = pd.read_sql("SELECT * FROM banks", engine)

# Merge tables
df = df.merge(banks, on="bank_id")

# -----------------------------------
# 1. REVIEW COUNT BY BANK
# -----------------------------------
review_counts = df["bank_name"].value_counts()

review_counts.plot(kind="bar")

plt.title("Review Count by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("outputs/review_count_by_bank.png")
plt.show()

# -----------------------------------
# 2. RATING DISTRIBUTION
# -----------------------------------
df.boxplot(column="rating", by="bank_name")

plt.title("Rating Distribution by Bank")
plt.suptitle("")
plt.xlabel("Bank")
plt.ylabel("Rating")

plt.tight_layout()
plt.savefig("outputs/rating_distribution.png")
plt.show()

# -----------------------------------
# 3. TOP KEYWORDS
# -----------------------------------
top_words = (
    df["review_text"]
    .str.lower()
    .str.split(expand=True)
    .stack()
    .value_counts()
    .head(15)
)

top_words.plot(kind="barh")

plt.title("Top Keywords in Reviews")
plt.xlabel("Frequency")

plt.tight_layout()
plt.savefig("outputs/top_keywords.png")
plt.show()

print("TASK 4 VISUALIZATIONS COMPLETE ✔")