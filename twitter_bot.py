import os
import tweepy
import random

# Twitter API credentials
consumer_key = os.environ[T5eSfLyVLha6IIwhXjL6zoGpB]
consumer_secret = os.environ[tH49mPLYYUSn4L8HHrNdXaibdBHib6PmxsT9UMtMsVKVe1FCmE]
access_token = os.environ[1899602226735439872-Ai7Jr50E4BrhQAKqcxTPdadnraQWPN]
access_token_secret = os.environ[V1YWIPn3vGZMr69NiK5tE69XkZ37KWnM3WKQJ9oV4oYNl]

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_random_tree():
    trees = ["Oak", "Maple", "Pine", "Birch", "Elm", "Willow", "Sycamore", "Ash"]
    return random.choice(trees)

def post_tree_tweet():
    tree = get_random_tree()
    tweet = f"Today's featured tree: {tree}"
    try:
        api.update_status(status=tweet)
        print(f"Posted tweet: {tweet}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    post_tree_tweet()
