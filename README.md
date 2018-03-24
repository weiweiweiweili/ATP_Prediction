# ATP Singles Outcome Prediction Flask App

## Project Objective 
This repo can be used to re-produce an web app that predict ATP game outcome based user input. The app is currently running at http://tennis.us-west-1.elasticbeanstalk.com.

## Team Members
* Developer: Wei Li
* Product Owner: Saurabh Tripathi
* QA: Michael Pauleen

## Project Charter

To investigate the applicability of machine learning methods to the prediction of professional tennis matches by training supervised learning models using tournament and players' information and players' in-game performance to propose betting strategies.

* Vision: to investigate the applicability of machine learning methods to the prediction of professional tennis matches and to improve understanding of deterministic features in predicting ATP Singles' game outcome
* Mission: predict game outcome by training supervised learning models (potentially logistic, SVM, neural network) using tournament and players' information and players' in-game performance based on a set of user selected features on tournament and players  
* Success criteria: a set of metrics for measuring overall model performance on predicting match results

## Data
The raw data is from [Github](https://github.com/JeffSackmann/tennis_atp). I used `Python` to do some EDA and clean the raw data (code in `models/EDA.ipynb`).

## Pivotal Tracker
[Link to Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2142964)

## App Demo Slides
The final demo slides deck is stored in `docs/Final_Presentation`.

## Logging
There are two sets of logging performed.
* `App/application.log` stores the logs of any user interaction with the application.
* logging for the modelling phase is done in console.

## Unit Testing
We performed unit testing for `App/models.py` file and unit test code is included in `App/unit_test.py`. The functions we tested are:
* `train_model`