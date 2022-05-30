#import library
import tweepy
import csv 

####input key dan token
consumer_key='mZ93svPwWm2RrmK2i9M6wj3eq'
consumer_secret='l7BVjFffkBmBLE2lGlAZoQANoqhsZ8XIsTYUcmLhipUxt2xEYW'

access_token='1493952640577044486-MUS4PCP2USphEem7R37z0Q0SJunI8E'
access_token_secret='cMO76uEAq1ICo49j0fhp3F8kIQHx33o405kTEBP0zqQEe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####MotoGP Mandalika
# Open/Create a file to append data
csvFile = open('3rd Meet (Thursday, February, 24th 2022)\Practice\Data\G20Indonesia.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
 
for tweet in tweepy.Cursor(api.search_tweets,q="#G20Indonesia",count=100,lang="id").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf8')])

# =========================

