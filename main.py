import tweepy
import time
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
REPLY_TO_TWEET_ID = os.getenv('REPLY_TO_TWEET_ID')


def TwitterClient():
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    return client


client = TwitterClient()
client.create_tweet(text=str(time.time()), in_reply_to_tweet_id=REPLY_TO_TWEET_ID)
