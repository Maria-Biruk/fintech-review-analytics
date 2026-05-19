import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv("data/raw/clean_reviews.csv")

# Clean column names
df.columns = df.columns.str.lower()

# Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:94128870@localhost:5432/bank_reviews"
)

print("Connected ✔")

# -------------------
# Insert banks table
# -------------------
banks_df = df[['bank']].drop_duplicates()
banks_df.columns = ['bank_name']
banks_df['app_name'] = banks_df['bank_name']

# Insert banks (avoid duplicates issue)
banks_df.to_sql('banks', engine, if_exists='append', index=False)

print("Banks inserted ✔")

# -------------------
# Get bank IDs
# -------------------
banks_db = pd.read_sql("SELECT * FROM banks", engine)

# -------------------
# Merge bank_id
# -------------------
df = df.merge(banks_db, left_on="bank", right_on="bank_name")

# -------------------
# Insert reviews table (FIXED)
# -------------------
reviews_df = df[[
    "bank_id",
    "review",
    "rating",
    "date",
    "source"
]]

# Rename columns to match DB schema
reviews_df.columns = [
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "source"
]

# Insert into PostgreSQL
reviews_df.to_sql('reviews', engine, if_exists='append', index=False)

print("Reviews inserted ✔")
print("TASK 3 COMPLETE 🚀")