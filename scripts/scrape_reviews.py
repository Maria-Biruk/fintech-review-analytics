from google_play_scraper import reviews, Sort
import pandas as pd

BANK_APPS = {
    "Bank_A": "com.example.bank1",
    "Bank_B": "com.example.bank2",
    "Bank_C": "com.example.bank3"
}

all_reviews = []

for bank, app_id in BANK_APPS.items():
    print(f"Scraping {bank}")

    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200
        )

        for r in result:
            all_reviews.append({
                "review": r.get("content", ""),
                "rating": r.get("score", None),
                "date": r.get("at", None),
                "bank": bank,
                "source": "Google Play"
            })

    except Exception as e:
        print(f"Error in {bank}: {e}")

df = pd.DataFrame(all_reviews)

print("COLUMNS:", df.columns)
print("SHAPE:", df.shape)

# SAFE CLEANING (NO CRASH)
if not df.empty:
    df = df.dropna(subset=["review", "rating"])
    df = df.drop_duplicates(subset=["review"])

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    df.to_csv("data/raw/clean_reviews.csv", index=False)

print("DONE")