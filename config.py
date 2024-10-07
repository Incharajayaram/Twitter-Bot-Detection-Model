import os
from dotenv import load_dotenv
import tweepy
from tweepy import API, OAuthHandler
from tweepy.errors import TweepyException, TooManyRequests, NotFound, Forbidden

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=False)

client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)
username = 'IncharaJ4'

try:
    user = client.get_user(username=username, user_fields=['created_at', 'public_metrics', 'description'])
    print(f"Username: {user.data.username}")
    print(f"ID: {user.data.id}")
    print(f"Bio: {user.data.description}")
    print(f"Account Created At: {user.data.created_at}")
    print(f"Followers Count: {user.data.public_metrics['followers_count']}")
    print(f"Following Count: {user.data.public_metrics['following_count']}")
    print(f"Tweet Count: {user.data.public_metrics['tweet_count']}")
    print(f"Listed Count: {user.data.public_metrics['listed_count']}")

    # Fetch recent tweets using v1.1
    tweets = api.user_timeline(screen_name=username, count=5)
    for tweet in tweets:
        print(f"{tweet.user.screen_name} said: {tweet.text}")

except TooManyRequests:
    print("Rate limit exceeded. Please wait and try again.")
except Forbidden:
    print("You don't have permission to access this resource.")
except NotFound:
    print("Resource not found.")
except TweepyException as e:
    print(f"Error during API request: {e}")