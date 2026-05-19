📊 Task 2: Sentiment and Thematic Analysis

This phase applied Natural Language Processing (NLP) techniques to analyze 2,735 Google Play Store reviews collected from Ethiopian banking applications.

The objective was to understand customer sentiment, identify recurring complaints, and extract meaningful themes that reflect user experience across different banks.

🧪 Techniques Used

The following NLP and analytical techniques were applied:

TextBlob Sentiment Analysis
Used to classify reviews into Positive, Neutral, and Negative categories based on polarity scores.
Keyword Frequency Analysis
Used to identify the most common terms appearing in customer feedback.
Thematic Grouping (Rule-based clustering)
Similar complaint terms were grouped to identify major issue categories.
TF-IDF (Term Frequency–Inverse Document Frequency)
Applied to negative reviews to extract high-importance complaint terms beyond simple word counts.
📈 Outputs

The analysis produced the following results:

Sentiment classification of all reviews:
Positive
Neutral
Negative
Identification of major complaint keywords such as:
Transaction failures
Login issues
Slow performance
App crashes
Update-related problems
Feature request insights including:
Faster transactions
Improved login reliability
Better app stability
Bank-level comparison of customer satisfaction and complaint intensity
🏦 Key Insight

The analysis reveals that systemic performance and transaction-related issues are common across all banks, indicating infrastructure and application stability challenges rather than isolated user complaints.

Among the three banks analyzed, Bank of Abyssinia (BOA) shows the highest concentration of negative sentiment, indicating greater customer dissatisfaction and potential retention risk.

🔍 Advanced Thematic Analysis (TF-IDF)

TF-IDF vectorization was applied specifically to negative reviews to identify high-impact complaint terms that are statistically important across the dataset.

This approach improved thematic extraction by reducing noise from frequently repeated but less meaningful words.

The analysis highlighted key operational issues, including:

Transaction and transfer failures
Mobile application performance issues
Login and authentication problems
Account access and usability challenges
🎯 Summary

Task 2 successfully transformed raw customer reviews into structured insights using NLP techniques. The results provide a strong foundation for data-driven decision-making by identifying both customer sentiment trends and underlying operational issues across Ethiopian banking applications.
