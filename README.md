# IPL-First-Innings-Score-Prediction
### https://ipl-scores-prediction.herokuapp.com/<br>
IPL First innings score predictor, a machine learning web app created with Flask on Heroku platform.

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#Technical-Aspect)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies used](#technologies-used)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)
  * [Credits](#credits)

## Overview
This is a flask web app which predicts the first inning score of Indian Premier League(IPL) with the help of Rgeressor model. The dataset is taken from https://github.com/codophobia/CricketScorePredictor credits to Shivam Mitra. It contains the score made on each ball of the matches played in IPL from 2008 to 2017.
This project helps the fantasy cricket fans out there.

## Motivation
Since childhood I am a great cricket fan. I played cricket at district and state level. Unfortunately 2020 is not a great year for all of us. We can't go outside from our home and enjoy the outdoor games. Last Year, I have started learning Data Science and Machine Learning course from online platform. So I thought to utilize this lockdown period to build something for a cricket fans using AI/ML. It is just a small initiative towards this.

## Technical Aspect:
This project is divided into two parts:
1) Trained a Machine Learning model using Regressor Models(Code is available in this repo).
2) Deployed the model using Flask on Heroku Platform.

## Installation
The Code is written in Python 3.7.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── static 
│   ├── styles.css
├── template
│   ├── index.html
|   ├── reult.html
├── IPL Score Prediction.ipynb
├── Procfile	
├── README.md
├── app.py
├── ipl.csv	
├── ipl_score_prediction1.pkl
├── requirements.txt
├── runtime.txt
```

## Technologies used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://i.imgur.com/gh8nX4U.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/)


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/nayan2112/IPL-First-Innings-Score-Prediction/issues) here by including your search query and the expected result

## Future Scope
• Consider venue as one of the aspect while creating a model.
• Add columns of the striker and non striker batsman who is playing at that moment.
• Implement this problem statement using Deep Learning(ANN).

## Credits
* Dataset: The dataset contains the score made on each ball of the matches played in IPL from 2008 to 2017.
* Dataset Link: https://github.com/codophobia/CricketScorePredictor (Credits to Shivam Mitra)
* Web App: https://ipl-scores-prediction.herokuapp.com/


