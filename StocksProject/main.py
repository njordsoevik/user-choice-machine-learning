# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:26:30 2020

@author: NjordSoevik
"""

#import custom files
import datasetAPI
import pandas as pd
import sys
import numpy as np
import sns_graphing
import torch_logistic
import seaborn as sns
import matplotlib.pyplot as plt

if __name__=="__main__":
    #ticker=str(input("Which ticker do you want to analyse? ")).upper()
    ticker='MSFT'
    key='8QMU1DNNWCWT1ZIA'
    features=['OpenPrice','HighPrice','LowPrice','Volume','MACD']
    target=['ClosingPrice']
    
    # Initialize class 
    df = datasetAPI.Dataframe(key,ticker,features,target)
    print('Raw Data: \n',df.rawData.head(5))
    print(df.rawData.shape[0])
    print('Features: \n',df.Features.sample(5))
    print('Target: \n',df.Target.head(5))
    
    # Now have features, target, do modeling
    
    torch_logistic.logisticRegression(df.Features.to_numpy(),df.Target.to_numpy(),df.Predict.to_numpy())
    
    #print(df.rawData.to_numpy())
    #sns_graphing.relplot(df.rawData)
    
    
    '''
    Drop first row of data and make prediction on it
    https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e
    https://hackernoon.com/linear-regression-in-x-minutes-using-pytorch-8eec49f6a0e2
    '''
    
    
    
    
    
    
    
    '''
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