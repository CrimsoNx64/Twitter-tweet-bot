#Twitter bot
#by crimson

import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

def tweet():
    message = "this will be tweeted"
    api.update_status(message)

while True:
    tweet()
    time.sleep(3600) # Tweet every hour
