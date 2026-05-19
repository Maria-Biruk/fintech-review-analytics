Project Overview

This project analyzes Google Play Store reviews from Ethiopian banking applications to identify customer satisfaction drivers, recurring complaints, and opportunities for product improvement.

The project combines:

Data scraping
Data preprocessing
Natural Language Processing (NLP)
Sentiment analysis
TF-IDF thematic analysis
PostgreSQL database engineering
Data visualization
Business recommendation generation

The project simulates a real-world analytics and data engineering workflow for fintech product analysis.

Business Objective

Omega Consultancy aims to help Ethiopian banks improve mobile banking services by analyzing customer feedback from Google Play Store reviews.

Mobile banking users frequently report issues related to:

Transaction failures
Login and OTP problems
App crashes
Slow performance
Update instability

This project transforms raw customer reviews into structured business insights that can support:

Product management decisions
Customer retention strategies
Feature prioritization
User experience improvements
Target Applications

The project analyzes reviews from:

Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank
Project Structure
fintech-review-analytics/
│
├── data/
│ └── raw/
│ ├── clean_reviews.csv
│ └── reviews_with_sentiment.csv
│
├── notebooks/
│
├── outputs/
│ ├── review_count_by_bank.png
│ ├── rating_distribution.png
│ └── top_keywords.png
│
├── reports/
│ ├── task2_insights.md
│ └── final_report.md
│
├── scripts/
│ ├── scrape_reviews.py
│ ├── sentiment_analysis.py
│ ├── tfidf_analysis.py
│ ├── load_to_postgres.py
│ └── task4_visuals.py
│
├── sql/
│ └── schema.sql
│
├── requirements.txt
├── README.md
└── .gitignore
Task 1: Data Collection and Preprocessing
Objective

Collect and preprocess customer reviews from Ethiopian banking applications using Google Play Store data.

Data Collection

Reviews were collected using the google-play-scraper Python library.

Data Source
Google Play Store
Applications Scraped
Commercial Bank of Ethiopia Mobile Banking
Bank of Abyssinia Mobile Banking
Dashen Super App
Fields Collected
Review text
Rating
Review date
Bank name
Source
Scraping Configuration
Language: English
Country: Ethiopia (country="et")
Sorting strategy: Most Relevant
Review target: 1000 reviews per bank
Data Preprocessing

The dataset was cleaned using the following preprocessing steps:

Removed missing values
Removed duplicate reviews
Standardized column names
Standardized date formats
Exported cleaned dataset to CSV
Final Dataset
Total reviews collected: 2735+
Output File
data/raw/clean_reviews.csv
Task 2: Sentiment and Thematic Analysis
Objective

Apply NLP techniques to identify customer sentiment, complaint themes, and product improvement opportunities.

NLP Techniques Used

1. TextBlob Sentiment Analysis

Used to classify reviews into:

Positive
Neutral
Negative 2. Keyword Frequency Analysis

Used to identify commonly repeated customer concerns.

3. TF-IDF Thematic Analysis

TF-IDF vectorization was applied to negative reviews to identify statistically important complaint themes.

This approach improved thematic extraction beyond simple word frequency analysis.

Key Complaint Themes

TF-IDF analysis identified major complaint areas such as:

Transaction failures
Transfer issues
Slow application performance
Login problems
Update instability
Account access issues
Bank-Level Insights
Commercial Bank of Ethiopia (CBE)
Strong positive sentiment due to large customer base
Complaints related to transaction speed and app responsiveness
Bank of Abyssinia (BOA)
Highest concentration of negative reviews
Frequent complaints regarding OTP and login failures
Dashen Bank
Most stable sentiment distribution
Better overall usability balance
Output Files
reports/task2_insights.md
scripts/tfidf_analysis.py
Task 3: PostgreSQL Database Engineering
Objective

Design and implement a PostgreSQL relational database to store cleaned review data.

Database Setup
Database Name
bank_reviews
Schema Design
Banks Table

Stores metadata about the banks.

Column Description
bank_id Primary Key
bank_name Bank name
app_name Application name
Reviews Table

Stores cleaned review data.

Column Description
review_id Primary Key
bank_id Foreign Key
review_text Customer review
rating User rating
review_date Review date
source Data source
ETL Pipeline

Python with SQLAlchemy and Pandas was used to:

Connect to PostgreSQL
Load cleaned CSV data
Insert bank metadata
Insert review records
Database Results
8205+ review records inserted successfully
Relational schema working correctly
Foreign key relationships verified
Verification Queries
Count Reviews Per Bank
SELECT b.bank_name, COUNT(_)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
Average Rating Per Bank
SELECT b.bank_name, AVG(r.rating)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;
Check Null Values
SELECT _
FROM reviews
WHERE review_text IS NULL
OR rating IS NULL
OR review_date IS NULL;
Output Files
scripts/load_to_postgres.py
sql/schema.sql
Task 4: Insights and Recommendations
Objective

Generate business-actionable insights supported by visualizations and customer feedback analysis.

Visualizations

The following visualizations were generated using Matplotlib:

Review Count by Bank
Rating Distribution by Bank
Top Keywords in Reviews

Visualization outputs are stored in:

outputs/
Business Insights
Commercial Bank of Ethiopia (CBE)
Satisfaction Drivers
Strong mobile banking adoption
Reliable core banking features
Pain Points
Slow transaction processing
Performance issues during peak usage
Recommendations
Improve backend scalability
Optimize transaction response times
Bank of Abyssinia (BOA)
Satisfaction Drivers
High customer engagement
Broad feature usage
Pain Points
OTP and login failures
Frequent app instability complaints
Recommendations
Improve authentication reliability
Enhance crash monitoring and testing
Dashen Bank
Satisfaction Drivers
Stable customer experience
Better usability balance
Pain Points
Limited advanced features
Update-related complaints
Recommendations
Introduce advanced digital banking tools
Improve update testing and deployment
Cross-Bank Comparison
BOA showed the highest concentration of negative feedback
CBE had the largest review volume
Dashen Bank demonstrated the most stable rating distribution
Technologies Used
Programming Language
Python
Libraries
pandas
matplotlib
sqlalchemy
psycopg2
textblob
scikit-learn
google-play-scraper
Database
PostgreSQL
Tools
VS Code
pgAdmin
Git
GitHub
Installation and Setup
Clone Repository
git clone https://github.com/Maria-Biruk/fintech-review-analytics.git
cd fintech-review-analytics
Install Dependencies
pip install -r requirements.txt
Configure PostgreSQL
Install PostgreSQL and pgAdmin
Create database:
CREATE DATABASE bank_reviews;
Run schema file:
sql/schema.sql
Run ETL Pipeline
python scripts/load_to_postgres.py
Run Visualizations
python scripts/task4_visuals.py
Conclusion

This project successfully implemented an end-to-end fintech analytics pipeline that combines:

Data scraping
Data preprocessing
NLP sentiment analysis
TF-IDF thematic extraction
PostgreSQL database engineering
Data visualization
Business recommendation generation

The analysis identified major customer concerns related to transaction reliability, authentication systems, and application stability.

The findings can support Ethiopian banks in improving digital banking experiences and prioritizing customer-focused product improvements.
