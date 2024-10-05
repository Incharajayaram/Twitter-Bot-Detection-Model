import os
from dotenv import load_dotenv
import tweepy


load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    print(f"Successfully authenticated as {user.screen_name}")
except Exception as e:
    print(f"An error occurred: {e}")