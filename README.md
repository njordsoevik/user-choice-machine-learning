# user-choice-machine-learning

## Description
This project will allow users to combine their choice of data sources, from Twitter posts to stock market indicators, and receive a trained neural network able to predict a another chosen data indicator. 
User facing RestAPI built with flask and neural networks optimized and trained with Pytorch.

## Motivation
1. With so many interesting data sources available online, I couldn't decide which data sources to commit a whole machine learning project to. 
2. I wanted some flexibility on the user's side on which data sources they wanted to train their model on, and what data to predict.
3. Instead of just outputting a prediction for the next X days, I want to provide the user to a trained model that they can use indefinitely.  
3. By allowing user input, the project exposes me to build an API (with Flask) and setting up a host for the API (AWS/Google Cloud).

## Constraints
1. Spare time. 

## Open Questions
1. Host this architecture on AWS or Google Cloud, still weighing the costs of each service.
2. What other data sources to incorporate.

## API 
### User Input
1. Features : Which data sources to combine and train PyTorch models. 
2. Target: The data to predict.

### API Output
1. Trained PyTorch model.

## Current data sources
1. Stock indicators with AlphaZero API.
2. Twitter with Twitter Developer API.
3. Instagram with Instagram Developer API.

