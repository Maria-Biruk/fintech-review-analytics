# Fintech Review Analytics

## Project Overview

This project analyzes user reviews from Google Play Store for three Ethiopian banking apps:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to collect, clean, and prepare customer reviews for sentiment analysis, thematic analysis, and product improvement recommendations.

---

## Task 1: Data Collection and Preprocessing

### Objective

Scrape user reviews from Google Play Store and preprocess them into a clean dataset ready for analysis.

---

## Data Collection Methodology

The `google-play-scraper` Python library was used to collect reviews from:

- Commercial Bank of Ethiopia Mobile Banking
- Bank of Abyssinia Mobile Banking
- Dashen Super App

### Fields Collected

The following fields were collected:

- Review Text
- Rating (1–5)
- Review Date
- Bank / App Name
- Source ("Google Play")

### Scraping Strategy

- Language: English
- Country: Ethiopia (`country="et"`)
- Review sorting: Most Relevant
- Review count target: 1000 reviews per bank

This helped ensure enough data was collected to exceed the minimum requirement of 400 reviews per bank.

---

## Final Dataset Summary

### Total Reviews Collected

**2735 reviews**

### Reviews Per Bank

- Commercial Bank of Ethiopia: 1000
- Bank of Abyssinia: 929
- Dashen Bank: 806

This exceeds the project KPI requirement of 1,200+ total reviews.

---

## Preprocessing Steps

The following cleaning steps were applied:

### 1. Remove Missing Values

Rows missing:

- review text
- rating

were removed.

### 2. Remove Duplicate Reviews

Duplicate reviews were removed using the review text field.

### 3. Normalize Dates

All dates were converted to:

`YYYY-MM-DD`

format for consistency.

### 4. Final Export

The cleaned dataset was saved as:

`data/raw/clean_reviews.csv`

---

## Limitations Encountered

Google Play Store review availability depends on app store API limitations.

Some apps returned fewer reviews than requested despite increasing the review count.

To improve coverage:

- review count was increased
- sorting changed from NEWEST to MOST_RELEVANT

This significantly improved final review collection.

---

## CI/CD Setup

GitHub Actions workflow was configured in:

`.github/workflows/unittests.yml`

This automatically runs:

```bash
pip install -r requirements.txt
```
