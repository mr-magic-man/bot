import os
import tweepy
import random

# Twitter API credentials
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_random_tree():
    trees = ["Oak", "Maple", "Pine", "Birch", "Elm", "Willow", "Sycamore", "Ash", "Cedar", "Redwood", "Spruce", "Fir", "Beech", "Poplar", "Cypress"]
    return random.choice(trees)

def post_tree_tweet():
    tree = get_random_tree()
    tweet = f"Today's featured tree: {tree} 🌳\n\nDid you know? Trees are vital for our planet's health, providing oxygen, absorbing CO2, and supporting biodiversity. #TreeFacts #Nature"
    try:
        api.update_status(status=tweet)
        print(f"Posted tweet: {tweet}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    post_tree_tweet()
