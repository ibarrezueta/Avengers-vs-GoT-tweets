from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "2kSzNO1KCKJBIFVa1Qa5q6CGz"
consumer_secret = "WG60uZKAj6eMVmW2U5nPtegO8scQQB8IcftKY4qhfEZgP0PVVN"
access_token = "1117533082968571904-iXUTQITNuRlde9xT08Mb18O4RyjqD7"
access_token_secret = "V8KweWjzflKZGAWPLLbjArheBO2F4DbeldkQ5zX6mgDVm"

class MyStreamListener(StreamListener):

    def on_status(self, status):
        print(status.text)

l = MyStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

myStreamListener = MyStreamListener()
myStream = Stream(auth, l)

myStream.filter(track=['avengers'])
