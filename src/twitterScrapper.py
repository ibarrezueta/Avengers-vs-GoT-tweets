from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sqlite3
import datetime
import time

consumer_key = 'consumer_key'
consumer_secret = `consumer_secret`
access_token = `access_token`
access_token_secret = 'access_token_secret'

def insertTweets(user, text, time, location, retweeted_status, conn):
    hashtag="tbd"
    InsertIntoTweet = "INSERT INTO Tweets(username, tweetLocation, tweetTime, tweetText, hashtag, isRetweet) VALUES(\"{B}\",\"{C}\",\"{D}\",\"{E}\",\"{F}\",\"{G}\");".format(B = user, C = location, D = time, E = text, F = hashtag, G = retweeted_status)
    try:
        result = conn.execute(InsertIntoTweet)
        conn.commit()
    except:
        print("err")

class MyStreamListener(StreamListener):
    conn = sqlite3.connect('twitterDB.sqlite3')
    def on_status(self, status, conn = sqlite3.connect('twitterDB.sqlite3')):
        print("created at: " + str(status.created_at))
        print("text: " + status.text)
        isRetweet = False
        try:
            if status.retweeted_status:
                isRetweet = True
        except:
            isRetweet = False
        insertTweets(status.user.screen_name, status.text, status.created_at, status.user.location, isRetweet, conn)

l = MyStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

while(True):
    try:
        myStreamListener = MyStreamListener()
        myStream = Stream(auth, l)

        myStream.filter(track=['avengers', 'gameofthrones'])
    except:
        print("You probably got kicked out, wait a few minutes")
        f = open("errorlog.txt", "a")
        currentDT = datetime.datetime.now()
        f.write(str(currentDT))
        f.close()
        time.sleep(1300)
