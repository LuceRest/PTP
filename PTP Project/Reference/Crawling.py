#import library
import tweepy
import csv 

####input key dan token
consumer_key='Q48TFzuRjTX10Fln0n0gYiBLz'
consumer_secret='z9O48rU0c9NlONMLzgLkSHdtQxi051HVbI92bRhtptaiYERm7Z'

access_token='1493952640577044486-kHKw9ek3LC872w8xjH2HymkaO6HkT7'
access_token_secret='DTUTFjg0dyWffqGJmOzA56x5TUcKwgsiRGl40LPUqcgB3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####MotoGP Mandalika
# Open/Create a file to append data
csvFile = open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
 
for tweet in tweepy.Cursor(api.search_tweets,q="#GoTo",count=50,lang="id").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf8')])

# =========================

