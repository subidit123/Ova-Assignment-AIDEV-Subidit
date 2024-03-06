import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK data (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define function to analyze sentiment of text
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
text = "I love this product! It's amazing!"
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")
