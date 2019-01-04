import twitter, re, datetime, pandas as pd
class twitterminer():
    request_limit = 20
    api = False
    data = []

    twitter_keys = {
        'consumer_key': 'h9AuPNFPeS0m4MPnvVdD00AS2', #add your consumer key
        'consumer_secret': 'sDhHXXejJA7PNPFmrNlWdDtqa7MwCAmci6rR4jz9M31w4ApB3V', #add your consumer secret key
        'access_token_key': '805863399032815616-ijcyfUVxoj7CGQCW6TjohKsFuXyQ4fl', #add your access token key
        'access_token_secret': 'aPUvZqCZRX3Cb2GA9fATUv9qvn0noMdb3giojl2iZcSrJ' #add your access token secret key
    }

    def __init__(self,  request_limit = 20):

        self.request_limit = request_limit

        # This sets the twitter API object for use internall within the class
        self.set_api()

    def set_api(self):

        self.api = twitter.Api(
            consumer_key = self.twitter_keys['consumer_key'],
            consumer_secret = self.twitter_keys['consumer_secret'],
            access_token_key = self.twitter_keys['access_token_key'],
            access_token_secret = self.twitter_keys['access_token_secret']
        )

    def mine_user_tweets(self, user=" set default user to get data from", mine_retweets=False):
        statuses = self.api.GetUserTimeline(screen_name=user, count=self.request_limit)
        data = []

        for item in statuses:
            mined = {
                'tweet_id': item.id,
                'handle': item.user.name,
                'retweet_count': item.retweet_count,
                'text': item.text,
                'mined_at': datetime.datetime.now(),
                'created_at': item.created_at,
            }

            data.append(mined)

        return data

    def find_followers(self, user_id_list):
        j_count = 0
        en_count = 0
        for user_id in user_id_list:
            try:
                user = self.api.GetUser(user_id=user_id)
            except twitter.error.TwitterError:
                pass
            #if user.lang != 'ja'
            representation = user.__repr__()
            print(representation)
            print(user.lang)
            print(user.followers_count)
            if user.lang == 'ja':
                j_count +=1
            if 'en' in user.lang:
                en_count +=1

        print("jap lang count", j_count)
        print("en lang count", en_count)

        return representation
