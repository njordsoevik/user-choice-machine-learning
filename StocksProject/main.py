# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:26:30 2020

@author: NjordSoevik
"""

#import custom files
import datasetAPI
import twitterAPI
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__=="__main__":
    ticker='MSFT'
    
    # User input
    features=['OpenPrice','HighPrice','LowPrice','Volume','MACD','TwitterName']
    target=['ClosingPrice']
    
    # All features
    stock_features=['OpenPrice','HighPrice','LowPrice','Volume','MACD','ClosingPrice']
    twitter_names = ["Microsoft"] 
            # Get Data
    if any(feature in features for feature in stock_features):
        df_stocks = datasetAPI.Dataframe(ticker,features,target)
        print('Raw Data: \n',df_stocks.rawData.head(5))
        print(df_stocks.rawData.shape[0])
        '''
        print('Features: \n',df.Features.head(5))
        print('Target: \n',df.Target.head(5))
        print('Predict: \n',df.Predict.head())
        '''
        
    
    if twitter_names:
            # Modeling
        Twit=twitterAPI.API(twitter_names)
        print(Twit.df_twitter.head())
    
    
    
    
    
    
    
'''

       self.Predict=self.rawData.iloc[[0]].drop(self.target_input,axis=1)
        
        # Getting Target and shift up by one

        self.Target = self.rawData[self.target_input].lt(self.rawData[self.target_input].shift()).astype(int)
        self.Features=self.rawData.drop(self.target_input,axis=1)

        self.Target = self.Target.iloc[1:]
        self.Features = self.Features.iloc[1:]
    Notes:
        
        django: https://www.youtube.com/watch?v=pLN-OnXjOJg&list=PL-51WBLyFTg38qZ0KHkJj-paDQAAu9HiP
            python manage.py startapp base
            add base to settings.py
            mkdir template/base inside of base
        
        
        
        
        
        
        
        
        
        
        Should allow option to pick two, show a relplot then do a binary classification, done with my algo
        
        For more than two, show relplots for all data point relations with the hue being target
        
        
        
        
        
        
        
        SEABORN:
            https://seaborn.pydata.org/tutorial/relational.html
            
            Melt can be useful for graphing all together
'''