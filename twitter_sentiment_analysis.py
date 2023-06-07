import tweepy
from textblob import TextBlob
import nltk

# Authenticate with Twitter API
def authenticate():
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

# Analyze the sentiment of a given text using TextBlob library
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Get tweets containing a certain keyword or hashtag
def get_tweets(api, query, count):
    tweets = []
    try:
        fetched_tweets = api.search(q=query, count=count)
        for tweet in fetched_tweets:
            parsed_tweet = {}
            parsed_tweet['text'] = tweet.text
            tweets.append(parsed_tweet)
        return tweets
    except tweepy.TweepError as e:
        print("Error : " + str(e))

# Analyze the sentiment of multiple tweets
def analyze_tweets_sentiment(tweets):
    sentiment_sum = 0
    for tweet in tweets:
        text = tweet['text']
        sentiment_sum += analyze_sentiment(text)
    return sentiment_sum/len(tweets)
