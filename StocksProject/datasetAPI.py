# -*- coding: utf-8 -*-
b"""
Spyder Editor

This is a temporary script file.
"""
import requests 
import pandas as pd
import json as js
import os
import numpy as np

class Dataframe:
    def __init__(self,ticker,inputs,target_input):
        key='8QMU1DNNWCWT1ZIA'
        stock_inputs_all=['OpenPrice','HighPrice','LowPrice','ClosingPrice','Volume']
        stock_indicator_inputs_all=['MACD']
        self.frames=[]
        self.key=key
        self.ticker=ticker
        self.inputs=inputs+target_input
        self.target_input=target_input
        
        stock_inputs=[item for item in self.inputs if item in '\n'.join(stock_inputs_all)]
        print('Stock inputs : \n',stock_inputs)
        stock_indicator_inputs=[item for item in self.inputs if item in '\n'.join(stock_indicator_inputs_all)]
        print('Other inputs : \n',stock_indicator_inputs)
        
        if stock_inputs:
            extract_needed=False
            for item in stock_inputs:
                if not os.path.exists("{}_{}.csv".format(self.ticker,item)):
                    extract_needed=True
                    break    
            if extract_needed==True:
                print('Extract is needed for stock price information! \n')
                self.getPrices(stock_inputs)
            else:
                for item in stock_inputs:
                    print("Extracting from Database: {}_{}.csv \n".format(self.ticker,item))
                    self.frames.append(pd.read_csv('{}_{}.csv'.format(self.ticker,item),index_col='date'))
                
        if stock_indicator_inputs: 
            extract_needed=False
            for item in stock_indicator_inputs:
                if not os.path.exists("{}_{}.csv".format(self.ticker,item)):
                    self.getOther(item)          
                else:
                    print("Extracting from Database: {}_{}.csv \n".format(self.ticker,item))
                    self.frames.append(pd.read_csv('{}_{}.csv'.format(self.ticker,item),index_col='date'))
        '''
        for i in range(0,len(self.frames)):
            print(self.frames[i].columns)
        '''
        # Merge all data into one table 
        
        self.rawData=merge(self.frames)
        
        # Drop NA values and create prediction row
        
        self.rawData.dropna(inplace=True)
        
    def getPrices(self,inputs):
        print('Getting stock data for: {}'.format(inputs))
        resp = requests.get(r'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}'.format(self.ticker,self.key))
        data = js.loads(resp.text)
        '''
        for key,value in data.items():
            print(key,value)
            print(data.keys())
        '''
        df = pd.DataFrame(data['Time Series (Daily)'])
        dataframe=df.transpose()
        dataframe.reset_index(inplace=True)
        dataframe.rename(columns={'index':'date','1. open':'OpenPrice','2. high':'HighPrice','3. low':'LowPrice','4. close':'ClosingPrice','5. volume':'Volume'},inplace=True)
        dataframe.set_index('date',inplace=True)
        # Filter by inputs
        # Save to CSV 
        for item in inputs:
            dataframe[item]=dataframe[item].astype(float)
            dataframe[item]=np.log(dataframe[item].values)
            print('Saving {}_{}.csv to file system!'.format(self.ticker,item))
            dataframe[item].to_csv('{}_{}.csv'.format(self.ticker,item))
            self.frames.append(dataframe[item])
    
    def getOther(self,item):
        print('Getting data for: {}'.format(item))
        if item=='MACD': 
            resp = requests.get('https://www.alphavantage.co/query?function=MACD&symbol={}&interval=daily&series_type=open&outputsize=full&apikey={}'.format(self.ticker,self.key))
            data = js.loads(resp.text)
            #print(data.keys())
            df = pd.DataFrame(data['Technical Analysis: MACD'])
            dataframe=df.transpose()
            dataframe.reset_index(inplace=True)
            dataframe.rename(columns={'index':'date'},inplace=True)
            rtD=dataframe[['date','MACD']]
            rtD.set_index('date',inplace=True)
            rtD.to_csv('{}_{}.csv'.format(self.ticker,'MACD'))
            self.frames.append(rtD)
'''
            dataframe[item].to_csv('{}_{}.csv'.format(self.ticker,item))
            self.frames.append(dataframe[item])

    def extractCSV(self,stock_inputs):
        return pd.read_csv("{}_{}.csv".format(self.ticker,item))
        
'''  
def merge(df_list):
    merged=df_list[0]
    for i in range(1,len(df_list)):
        merged=pd.merge(merged,df_list[i], on='date', how='outer')
            #    self.RawData.dropna(inplace=True)
    return merged

def comparePrevious(x):
    if x.shift()>x.shift(1):
        return 1
    else:
        return 0

