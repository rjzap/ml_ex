import tweepy
from tweepy import OAuthHandler

consumer_key = 'V4BS0ltuZ3Mie32UVdUVVU3ha'
consumer_secret = 'YXZtLKLSrCCUgwT1UdNnprIiOGo3qi4CkDKTLu3z2BWkKEE0Wz8'
access_token = '887699948480942080-qMwttUeXt0fydzVW0YRV9J38FXsOPjA'
access_secret = '3CRP9rnYyYuHWU0bhu0VpN87Nq6V41bUlxslsMeTJS9DU'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
