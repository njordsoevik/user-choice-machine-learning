# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:49:47 2020

@author: NjordSoevik
"""
import re
import tweepy as tp
from textblob import TextBlob
import pandas as pd
import os
#https://www.toptal.com/python/twitter-data-mining-using-python



class API():
    def __init__(self,names):
        consumer_key='8vVhqwweAVUtaxDIDax9wmMfK'
        consumer_secret='sO6bvD1Jul1tbHleSnrnG1miK59y4S3QXWHej7WhNJ2QJwkVlL'
        access_token='1225191361835622402-WFJgDJwKWAt2JO2Mzw7WDTv3AYJqpu'
        access_token_secret='nciJzGVlBEJCxeXVJc823VMVv3VY8qyptreyjAGizoWrh'
        frames=[]
        # Creating the authentication object
        self.auth = tp.OAuthHandler(consumer_key, consumer_secret)
        # Setting your access token and secret
        self.auth.set_access_token(access_token, access_token_secret)
        # Creating the API object while passing in auth information
        self.auth = tp.API(self.auth) 
        
        
        for name in names:
            # If data does not already exist, GET data
            if not os.path.exists(os.getcwd()+'/twitter_data/{}_sentiment.csv'.format(name)):
                tweetlist = self.get(name)
                df_sentiment = self.analyze(tweetlist,name)
                df_sentiment= df_sentiment.groupby('date').mean()
                df_sentiment.to_csv(os.getcwd()+'/twitter_data/{}_sentiment.csv'.format(name),index=True)
                frames.append(df_sentiment)
            else:
                df_sentiment = pd.read_csv(os.getcwd()+'/twitter_data/{}_sentiment.csv'.format(name))
                frames.append(df_sentiment)
        
        self.df_twitter = frames[0]
        if len(frames)>1:
            for i in range(1,len(frames)):
                self.df_twitter=pd.merge(self.df_twitter,frames[i], on='date', how='outer')
        
    def get(self,name):
        tweetlist=[]
        for status in tp.Cursor(self.auth.user_timeline, name).items():
            # Clean text
            tweet=status.text.encode('utf-8')
            text=self.cleantweet(str(tweet))
            # Clean date
            date=str(status.created_at).split(' ')[0]
            # Append list
            tweetlist.append([date,text])
        
        print('Extracted {} many tweets from {} twitter feed today'.format(len(tweetlist),name))
        print('Most recent tweet: {}'.format(tweetlist[0]))
        return tweetlist
        
        
    def cleantweet(self,txt):
        txt=txt.lower()
        return ' '.join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
        return txt
        
    def analyze(self,tweets,name):
        dates=[]
        sentiment_objects=[]
        for lst in tweets:
            dates.append(lst[0])
            sentiment_objects.append(TextBlob(lst[1]))
        sentiment_objects= [[x.polarity,str(x)] for x in sentiment_objects]
        df_date=pd.DataFrame(dates, columns=['date'])
        df_sentiment=pd.DataFrame(sentiment_objects,columns=['polarity_'+name,'tweet_'+name])
        df_sentiment['date']=df_date['date']
        df_sentiment.set_index('date',inplace=True)
        return df_sentiment
 
