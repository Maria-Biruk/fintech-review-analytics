import os
import pandas as pd
from google_play_scraper import reviews, Sort

# create folder safely
os.makedirs("data/raw", exist_ok=True)

BANK_APPS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in BANK_APPS.items():
    print(f"Scraping {bank}...")

    try:
        result, _ = reviews(
            app_id,
            lang="en",
            country="et",
           sort=Sort.MOST_RELEVANT,
            count=1000
        )

        for r in result:
            all_reviews.append({
                "review": r.get("content"),
                "rating": r.get("score"),
                "date": r.get("at"),
                "bank": bank,
                "source": "Google Play"
            })

    except Exception as e:
        print(f"Error scraping {bank}: {e}")

df = pd.DataFrame(all_reviews)

print("Before cleaning:", df.shape)

# remove missing values
df = df.dropna(subset=["review", "rating"])

# remove duplicates
df = df.drop_duplicates(subset=["review"])

# normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

print("After cleaning:", df.shape)

# save final dataset
df.to_csv("data/raw/clean_reviews.csv", index=False)

print("DONE: clean_reviews.csv created successfully")
