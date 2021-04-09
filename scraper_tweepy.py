#using tweepy


import tweepy
from tweepy import OAuthHandler
import pandas as pd
import json

def scraper_tweepy(dict,df1,begin_date,marque):

    access_token = '1267842704739835907-04jDrMDj3zwXIDTDQ57nBLUBb036Yk'
    access_token_secret = 'KJI92QvsZuUFxJWVyjdwenr2iywChWG2Sr7dk0u84zwCp'
    consumer_key = 'EFEobkZsc55l02v232XY43jtX'
    consumer_secret = 'p9CFzTx4my0sd5u7Fg5O9TE2d4hJOtad7ev19PD0fzb4HUGAOU'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    tweets = []

    count = 1

    for tag in dict:

        for tweet in tweepy.Cursor(api.search, q=tag, count=450, since=begin_date).items(5000):

            print(count)
            count += 1

            try:
                data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'],
                        tweet.user._json['created_at'], tweet.entities['urls'],tweet.lang]
                data = tuple(data)
                tweets.append(data)

            except tweepy.TweepError as e:
                print(e.reason)
                continue

            except StopIteration:
                break

    df = pd.DataFrame(tweets,
                      columns=['created_at', 'tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date',
                               'urls','language'])
    df['marque']=marque
    df=pd.concat([df1, df], ignore_index=True)

    return df