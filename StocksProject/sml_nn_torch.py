# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:23:42 2020

@author: NjordSoevik
"""

import torch
print(torch)
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split

def logisticRegression(X,y,predict):
    # Scale
    n_samples, n_features=X.shape
    
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)
    sc = StandardScaler()
    
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    
    predict=torch.from_numpy(predict.astype(np.float32))
    X_train=torch.from_numpy(X_train.astype(np.float32))
    X_test=torch.from_numpy(X_test.astype(np.float32))
    y_train=torch.from_numpy(y_train.astype(np.float32))
    y_test=torch.from_numpy(y_test.astype(np.float32))
    
    # 1) Model
    class LogisticRegression(nn.Module):
        def __init__(self,n_input_features):
            super(LogisticRegression, self).__init__()
            self.linear1=nn.Linear(n_input_features,n_input_features+1)
            self.linear2=nn.Linear(n_input_features+1,1)
            self.sigmoid=nn.Sigmoid()
        def forward(self,x):
            x=self.linear1(x)
            x=self.sigmoid(x)
            x=self.linear2(x)
            x=self.sigmoid(x)
            return x
    
    model=LogisticRegression(n_features)
    if torch.cuda.is_available():
        model.cuda()
        
    # 2) loss and Optimizer
    learning_rate=5e-2
    criterion=nn.BCELoss() # Binary Cross Entropy Loss
    optimizer=torch.optim.SGD(model.parameters(),learning_rate) # Stocrastic Gradient Descent
    
    # 3) Training Loop
    epochs=100
    for epoch in range(epochs):
        # forward pass and loss
        y_predicted=model(X_train)
        loss = criterion(y_predicted,y_train)
        
        # backward pass 
        loss.backward()
        
        # updates
        optimizer.step()
        
        # zero gradients
        optimizer.zero_grad()
        
        if (epoch+1)%10==0:
            print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

    with torch.no_grad():   
        # get accuracy
        y_predicted=model(X_test)
        
        # round up the predictions when .5 and above
        y_predicted_cls=y_predicted.round()
    
        acc = y_predicted_cls.eq(y_test).sum()/float(y_test.shape[0])
        print(f'accuracy = {acc:.4f}')
        
        # Save Model
        # https://pytorch.org/tutorials/beginner/saving_loading_models.html 
        torch.save(model.state_dict(),'myModel.pt')
    
    print(predict.shape,X_train.shape)
    prediction=model.forward(predict)
    print(prediction)

        
'''
change learning rate, epochs, and optimizer for better results
'''