# T20-First-Innings-Score-Prediction
### <br>
T20 First innings score predictor, a machine learning web app created with Flask on Streamlit platform.

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#Technical-Aspect)
  * [Installation](#installation)
  * [Deployement on Streamlit](#deployement-on-Streamlit)
  * [Directory Tree](#directory-tree)
  * [Technologies used](#technologies-used)
  * [Future scope of project](#future-scope)
  * [Credits](#credits)

## Overview
This is a Flask web app which predicts the First Innings Score of a T20 International match with the help of a model based on Random Forest Regressor algorithm . The dataset is taken from https://cricsheet.org/matches . It contains ball-by-ball data for more than 1400 T20 Internationals played till date.

## Motivation
The goal of building a cricket score prediction model is to provide fans, coaches, and analysts with insights into the potential outcome of a match and to help them make informed decisions. By using machine learning techniques, it is possible to identify patterns and trends in past performance data and use them to predict the final score of a match with a high degree of accuracy.

## Technical Aspect:
This project is divided into two parts:
1) Trained a Machine Learning model using RF Regressor Model (Code is available in this repo).
2) Deployed the model on Streamlit Platform.

## Installation
The Code is written in Python 3.7.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Streamlit
Login or signup in order to create a virtual app. Connect your Github profile to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://streamlit.io/)

Our next step would be to follow the instruction given on [Streamlit Documentation](https://docs.streamlit.io/library/get-started) to deploy the web app.

## Directory Tree 
```

├── T20 Score Prediction.ipynb	
├── README.md
├── app.py
├── T20 International Dataset.csv	
├── score_prediction1.pkl
├── requirements.txt
├── runtime.txt
```

## Technologies used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/)  [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://i.imgur.com/gh8nX4U.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/)



## Future Scope
• Consider venue as one of the aspects while creating the prediction model.
• Add columns of the striker and non striker batsman who is playing at that moment.
• Implement this problem statement using Deep Learning (ANN).

## Credits
* Dataset: It contains ball-by-ball data for more than 1400 T20 Internationals played till date.
* Dataset Link: https://cricsheet.org/matches
* Web App: https://ipl-scores-prediction.herokuapp.com/


